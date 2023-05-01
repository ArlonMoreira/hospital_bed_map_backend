from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiExample
from .serializer import HospitalSerializer
from .examples import RESPONSE, REQUESTS

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
        serializer = self.serializer_class(data=request.data, context={'user': request.user})

        if not(serializer.is_valid()):
            return Response({'message': 'Falha ao cadastrar hospital, verifique os dados inseridos e tente novamente.', 'data':[serializer.errors]}, status=status.HTTP_400_BAD_REQUEST)

        serializer_data = self.serializer_class(serializer.save()).data

        return Response({'message': 'Hospital cadastrado.', 'data': [serializer_data]}, status=status.HTTP_201_CREATED)
