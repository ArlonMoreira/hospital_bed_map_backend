from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from hospital_bed_map_backend.beds.api.serializer import BedsSerializer
from hospital_bed_map_backend.beds.models import Beds, TypeOccupation, Type
from hospital_bed_map_backend.sectors.models import Sectors

class BedsView(generics.GenericAPIView):
    serializer_class = BedsSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        serializer = self.serializer_class(data=request.data, context={'user': request.user})

        if not(serializer.is_valid()):
            return Response({'message': 'Falha ao cadastrar o leito , verifique os dados e tente novamente.', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.save()
        sector = Sectors.objects.filter(id=data.sector.id).first()
        typeOccupation = TypeOccupation.objects.filter(description=data.type_occupation).first()
        type = Type.objects.filter(description=data.type).first()

        result = {
            'id': data.pk,
            'hospital_id': sector.hospital.id,
            'sector_id': sector.id,
            'name': data.name,
            'type_occupation_status': typeOccupation.status,
            'type_occupation_description': typeOccupation.description,
            'type': type.description,
            'is_active': data.is_active,
            'is_extra': data.is_extra
        }

        return Response({'message': 'Leito cadasrtado com sucesso', 'data': [result]}, status=status.HTTP_200_OK)