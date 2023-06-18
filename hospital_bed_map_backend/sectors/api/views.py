from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiTypes
from .serializer import SectorsSerializer
from ..models import Hospital, Sectors, TypeAccommodation
from .examples import REQUESTS_POST, RESPONSE_POST, RESPONSE_GET

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
        description='<p>Este endpoint possibilita a obtenção de dados de um ou mais setores existentes no sistema. Ao efetuar uma requisição sem a inclusão de um identificador (id), serão retornados os dados de todos os hospitais existentes no sistema. No entanto, ao especificar o identificador (id) na URL, somente os dados do hospital correspondente serão retornados.</p>\
        <i>This endpoint makes it possible to obtain data from one or more sectors existing in the system. When making a request without including an identifier (id), data from all hospitals in the system will be returned. However, when specifying the identifier (id) in the URL, only the corresponding hospital data will be returned.</i>',
        responses={
            200: OpenApiTypes.OBJECT,
            401: OpenApiTypes.OBJECT,
            404: OpenApiTypes.OBJECT
        },
        examples=RESPONSE_GET
    )
    def get(self, request, id=None):
        if id is None:
            hospital = Hospital.objects.all()
        else:
            hospital = Hospital.objects.filter(id=id)
            if not(hospital.exists()):
                return Response({'message': 'Hospital {} não encontrado'.format(id)}, status=status.HTTP_404_NOT_FOUND)
            
        data = Sectors.objects.filter(hospital=hospital.first().id)
        serializer = self.serializer_class(data, many=True)
        
        return Response({'message': 'Dados obtidos com sucesso.', 'data': serializer.data}, status=status.HTTP_200_OK)
    
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