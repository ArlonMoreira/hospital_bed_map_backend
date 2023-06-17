from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiTypes
from .serializer import SectorsSerializer
from ..models import Hospital
from .examples import REQUESTS_POST, RESPONSE_POST

class SectorsView(generics.GenericAPIView):
    serializer_class = SectorsSerializer
    permission_classes = [IsAuthenticated]

    def handle_exception(self, exc):
        if isinstance(exc, NotAuthenticated):
            return Response({'message': 'As credenciais de autenticação não foram fornecidas.'}, status=status.HTTP_401_UNAUTHORIZED)
        if isinstance(exc, AuthenticationFailed):
            return Response({'message': 'As credenciais de autenticação são inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)        

        return super().handle_exception(exc)

    @extend_schema(
        description='<p>Este endpoint possibilita o criação de um setor de internação. Vale ressaltar que o setor consiste em um agrupamento de leitos hospitalares e possui como característica um tipo de acomodação em específico.</p>\
        <i>This endpoint enables the creation of a hospitalization sector. It is worth mentioning that the sector consists of a group of hospital beds and has a specific type of accommodation as a characteristic.</i>',
        responses={
            201: OpenApiTypes.OBJECT,
            400: OpenApiTypes.OBJECT,
            401: OpenApiTypes.OBJECT,
            404: OpenApiTypes.OBJECT,
        },
        examples=RESPONSE_POST,
        request=REQUESTS_POST
    )
    def post(self, request, id=None):
        if not(Hospital.objects.filter(id=id).exists()):
            return Response({'message': 'Hospital não encontrado ou não informado.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(data=request.data, context={'user': request.user, 'hospital': id})
        if not(serializer.is_valid()):
            return Response({'message': 'Falha ao cadastrar o setor de internação, verifique os dados inseridos e tente novamente.', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer_data = self.serializer_class(serializer.save()).data
        
        return Response({'message': 'Setor cadastrado.', 'data': [serializer_data]}, status=status.HTTP_200_OK)