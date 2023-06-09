from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiTypes
from .serializer import HospitalSerializer
from ..models import Hospital
from .examples import RESPONSE, REQUESTS, RESPONSE_GET
import re

class HospitalView(generics.GenericAPIView):
    serializer_class = HospitalSerializer
    permission_classes = [IsAuthenticated]

    def handle_exception(self, exc):
        if isinstance(exc, NotAuthenticated):
            return Response({'message': 'As credenciais de autenticação não foram fornecidas.'}, status=status.HTTP_401_UNAUTHORIZED)
        if isinstance(exc, AuthenticationFailed):
            return Response({'message': 'As credenciais de autenticação são inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)        

        return super().handle_exception(exc)
    
    @extend_schema(
        description='<p>Este endpoint possibilita a obtenção de dados de um ou mais hospitais existentes no sistema. Ao efetuar uma requisição sem a inclusão de um identificador (id), serão retornados os dados de todos os hospitais existentes no sistema. No entanto, ao especificar o identificador (id) na URL, somente os dados do hospital correspondente serão retornados.</p></br>\
        <i>This endpoint makes it possible to obtain data from one or more hospitals in the system. When making a request without including an identifier (id), data from all hospitals in the system will be returned. However, when specifying the identifier (id) in the URL, only the corresponding hospital data will be returned.</i>',
        responses={
            200: OpenApiTypes.OBJECT,
            401: OpenApiTypes.OBJECT,
            404: OpenApiTypes.OBJECT
        },
        examples=RESPONSE_GET
    )
    def get(self, request, id=None):
        
        if id is None:
            serializer = self.serializer_class(Hospital.objects.all(), many=True)
            return Response({'message': 'Dados obtidos com sucesso.', 'data': serializer.data}, status=status.HTTP_200_OK)
        
        hospital = Hospital.objects.filter(id=id).first()
        if hospital is None:
            return Response({'message': 'Hospital {} não encontrado'.format(id)}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(hospital)
        return Response({'message': 'Dados obtidos com sucesso.', 'data': [serializer.data]}, status=status.HTTP_200_OK)
    
    @extend_schema(
        description='<p>Este é um endpoint que permite a criação de um novo objeto Hospital no sistema. Para acessá-lo, é necessário que o usuário esteja autenticado. O endpoint recebe uma requisição HTTP POST com os dados do hospital a ser cadastrado, em formato JSON.</p>\
        <i>This is an endpoint that allows the creation of a new Hospital object in the system. To access it, the user must be authenticated. The endpoint receives an HTTP POST request with the data of the hospital to be registered, in JSON format.</i>',
        responses={
            201: OpenApiTypes.OBJECT,
            400: OpenApiTypes.OBJECT,
            401: OpenApiTypes.OBJECT,
        },
        examples=RESPONSE,     
        request=REQUESTS
    )    
    def post(self, request, *args, **kwargs):
        #Format CNPJ field
        if(str(request.data['cnpj']) != ""):
            cnpj = re.sub(r'\D', '', str(request.data['cnpj'])).zfill(14)
            request.data['cnpj'] = '{}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])
        #Format CNES field
        if(str(request.data['cnes']) != ""):
            request.data['cnes'] = str(request.data['cnes']).zfill(7)

        serializer = self.serializer_class(data=request.data, context={'user': request.user})

        if not(serializer.is_valid()):
            return Response({'message': 'Falha ao cadastrar hospital, verifique os dados inseridos e tente novamente.', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer_data = self.serializer_class(serializer.save()).data

        return Response({'message': 'Hospital cadastrado.', 'data': [serializer_data]}, status=status.HTTP_201_CREATED)
