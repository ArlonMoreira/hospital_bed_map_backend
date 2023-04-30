from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .serializer import HospitalSerializer

class HospitalView(generics.GenericAPIView):
    serializer_class = HospitalSerializer
    permission_classes = [IsAuthenticated]
            
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'user': request.user})

        if not(serializer.is_valid()):
            return Response({'message': 'Falha ao criar hospital, verifique os dados inseridos e tente novamente.', 'data':[serializer.errors]}, status=status.HTTP_400_BAD_REQUEST)

        serializer_data = self.serializer_class(serializer.save()).data

        return Response({'message': 'Hospital cadastrado.', 'data': [serializer_data]}, status=status.HTTP_201_CREATED)
