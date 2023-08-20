from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from hospital_bed_map_backend.beds.api.serializer import BedsActiveUpdateSerializer, BedsStatusUpdateSerializer, BedsListSerializer, TypeSerializer, BedsSerializer, TypeOccupationSerializer
from hospital_bed_map_backend.beds.models import TypeOccupation, Type, Beds
from hospital_bed_map_backend.sectors.models import Sectors
from django.db.models import F

class TypeView(generics.GenericAPIView):
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Type.objects.all()
        serializer = self.serializer_class(data, many=True).data
        
        return Response({'message': 'Dados recuperados com sucesso', 'data': serializer}, status=status.HTTP_200_OK)

class TypeOccupationView(generics.GenericAPIView):
    serializer_class = TypeOccupationSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = TypeOccupation.objects.all()
        serializer = self.serializer_class(data, many=True).data

        return Response({'message': 'Dados recuperados com sucesso', 'data': serializer}, status=status.HTTP_200_OK)

class BedsListView(generics.GenericAPIView):
    serializer_class = BedsListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, sector=None):

        data = Beds.objects.filter(sector=sector)\
                .values('id', 'sector__hospital', 'sector', 
                'name', 'type_occupation', 'type_occupation__status', 'type_occupation__description',
                'type__description', 'is_active', 'is_extra')\
                .annotate(  hospital_id=F('sector__hospital'), 
                            sector_id=F('sector'),
                            type_occupation_id=F('type_occupation'),
                            type_occupation_status=F('type_occupation__status'),
                            type_occupation_description=F('type_occupation__description'),
                            type=F('type__description'))
        
        serializer = self.serializer_class(data, many=True).data

        return Response({'message': 'Dados recuperados com sucesso', 'data': serializer}, status=status.HTTP_200_OK)
    
class BedsUpdateActiveView(generics.GenericAPIView):
    serializer_class = BedsActiveUpdateSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, bed=None):
        bed = Beds.objects.filter(id=bed)

        if bed.exists():
            serializer = self.serializer_class(bed, data=request.data, context={'user': request.user})
            if(not(serializer.is_valid())):
                return Response({'message': 'Falha ao atualizar os dados do leito.', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            serializer_data = self.serializer_class(serializer.save()).data
            
        else:
            return Response({'message': 'Leito não encontrado.'}, status=status.HTTP_404_NOT_FOUND)  

        return Response({'message': 'Dados do leito atualizado com sucesso.', 'data': [serializer_data]}, status=status.HTTP_200_OK)

class BedsUpdateStatusView(generics.GenericAPIView):
    serializer_class = BedsStatusUpdateSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, bed=None):
        bed = Beds.objects.filter(id=bed)

        if bed.exists():
            serializer = self.serializer_class(bed, data=request.data, context={'user': request.user})
            if(not(serializer.is_valid())):
                return Response({'message': 'Falha ao atualizar os dados do leito.', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            serializer_data = self.serializer_class(serializer.save()).data
            typeOccupation = TypeOccupation.objects.filter(pk=serializer_data['type_occupation']).first()
            data = {
                'id': serializer_data['id'],
                'type_occupation_id': serializer_data['type_occupation'],
                'type_occupation_status': typeOccupation.status,
                'type_occupation_description': typeOccupation.description
            }
            
        else:
            return Response({'message': 'Leito não encontrado.'}, status=status.HTTP_404_NOT_FOUND) 
        
        return Response({'message': 'Dados do leito atualizado com sucesso.', 'data': [data]}, status=status.HTTP_200_OK)
    
class BedsDeleteView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, bed=None):
        data = Beds.objects.filter(id=bed)

        if(data.exists()):
            id_leito = data.first().pk
            if(data.values('type_occupation__status').first()['type_occupation__status'] == 'OCUPADO'):
                return Response({'message': 'Leito ocupado não pode ser deletado.'}, status=status.HTTP_400_BAD_REQUEST)
            data.delete()

        else:
            return Response({'message': 'Leito não encontrado.'}, status=status.HTTP_404_NOT_FOUND) 

        return Response({'message': 'Dados do leito removido com sucesso.', 'data': [{'id': id_leito}]}, status=status.HTTP_200_OK)
    
class BedsView(generics.GenericAPIView):
    serializer_class = BedsSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        serializer = self.serializer_class(data=request.data, context={'user': request.user})

        if not(serializer.is_valid()):
            return Response({'message': 'Falha ao cadastrar o leito , verifique os dados e tente novamente.', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.save()
        sector = Sectors.objects.filter(id=data.sector.id).first()

        if data.type_occupation is None:
            typeOccupation = TypeOccupation.objects.filter(status='VAGO').first()
        else:
            typeOccupation = TypeOccupation.objects.filter(description=data.type_occupation).first()
    
        if data.type is None:
            type = None
        else:
            type = Type.objects.filter(description=data.type).first().description

        result = {
            'id': data.pk,
            'hospital_id': sector.hospital.id,
            'sector_id': sector.id,
            'name': data.name,
            'type_occupation_id': typeOccupation.id,
            'type_occupation_status': typeOccupation.status,
            'type_occupation_description': typeOccupation.description,
            'type': type,
            'is_active': data.is_active,
            'is_extra': data.is_extra
        }

        return Response({'message': 'Leito cadasrtado com sucesso', 'data': [result]}, status=status.HTTP_200_OK)