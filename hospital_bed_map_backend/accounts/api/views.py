from django.contrib.auth import authenticate, login, logout
from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiExample
from .serializer import LoginSerializer
from ..utils import get_tokens_for_user

#Customiza a atualização do token para retornar também o refresh token como resposta
class RefreshTokenView(TokenRefreshView):

    def handle_exception(self, exc):
        if isinstance(exc, InvalidToken) or isinstance(exc, TokenError):
            return Response({'message': 'Sua sessão foi encerrada.', 'data': {}}, status=status.HTTP_401_UNAUTHORIZED)
        return super().handle_exception(exc)    
 
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh_token = serializer.validated_data.get('refresh')
        refresh = RefreshToken(refresh_token)
        data = {
            'message': 'Sessão renovada.',
            'data': {
                'refresh': request.data['refresh'],
                'access': str(refresh.access_token),      
            }
        }

        return Response(data)

#Class responsible for performing user authentication via REST API
class LoginView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not(serializer.is_valid()):
            return Response({'message': 'Certifique-se que o usuário ou senha estão corretos.', 'data': serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = serializer.data

        '''
        #https://docs.djangoproject.com/en/4.1/topics/auth/default/
        authenticate() method checks if the authentication credentials are valid. returns a User object if
        the credentials are valid for a backend. If credentials are not valid for any backend
        or if a backend throws PermissionDe
        '''        
        user = authenticate(request, username=serializer['username'], password=serializer['password'])
        if user is not None:
            '''
            The login() method logs in and saves the user ID to the session, using Django's session framework.
            '''
            login(request, user)
            data = get_tokens_for_user(user)

            return Response({'message': 'Usuário autenticado com sucesso.', 'data': data}, status=status.HTTP_200_OK)
        
        return Response({'message': 'Certifique-se que o usuário ou senha estão corretos.', 'data': {}}, status=status.HTTP_401_UNAUTHORIZED)

#Class responsible for terminating the session
class LogoutView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        logout(request)
        return Response({'message': 'Sucesso ao finalizar à sessão.', 'data': []}, status=status.HTTP_200_OK)
