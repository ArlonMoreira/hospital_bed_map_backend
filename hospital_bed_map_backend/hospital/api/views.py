from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiExample
from .serializer import HospitalSerializer

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
        description='',
        responses={
            201: OpenApiTypes.OBJECT,
            400: OpenApiTypes.OBJECT,
            401: OpenApiTypes.OBJECT,
        },
        examples=[
            OpenApiExample(
                "Success",
                description='<p>Sucesso ao cadastrar um novo hospital.</p>\
                <i>Success in registering a new hospital.</i>',
                value={
                    'message': 'Hospital cadastrado.',
                    'data': [
                        {
                            "id": 0,
                            "name": "string",
                            "acronym": "string",
                            "is_active": True
                        }                        
                    ]
                },
                response_only=True,
                status_codes=["201"],        
            ),
            OpenApiExample(
                "Bad Request",
                description='<p>Falha ao cadastrar hospital pois os parâmetros informados não estão conforme o esperado.</p>\
                <i>Failed to register hospital because the informed parameters are not as expected.</i>',
                value={
                    'message': 'Falha ao cadastrar hospital, verifique os dados inseridos e tente novamente.',
                    'data': {
                        "name": [
                            "O nome do hospital informado é relativamente curto.",
                            "Hospital com este none já existe.",
                            "Este campo não pode ser nulo.",
                            "Este campo não pode ser em branco.",
                            "Este campo é obrigatório."
                        ]                                            
                    }
                },
                response_only=True,
                status_codes=["400"],        
            ),                       
        ],     
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Nome completo do hospital", "required": True, "min_lengh": 10},
                    "acronym": {"type": "string", "description": "Sigla do hospital", "required": False},
                    "is_active": {"type": "boolean", "description": "Hospital será criado como ativo ou não", "required": False, "default": True}
                }
            }            
        }
    )    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'user': request.user})

        if not(serializer.is_valid()):
            return Response({'message': 'Falha ao cadastrar hospital, verifique os dados inseridos e tente novamente.', 'data':[serializer.errors]}, status=status.HTTP_400_BAD_REQUEST)

        serializer_data = self.serializer_class(serializer.save()).data

        return Response({'message': 'Hospital cadastrado.', 'data': [serializer_data]}, status=status.HTTP_201_CREATED)
