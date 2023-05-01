from drf_spectacular.utils import OpenApiExample

REQUESTS = {
    "application/json": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Nome completo do hospital", "required": True, "min_lengh": 10},
            "acronym": {"type": "string", "description": "Sigla do hospital", "required": False},
            "is_active": {"type": "boolean", "description": "Hospital será criado como ativo ou não", "required": False, "default": True}
        }
    }            
}

RESPONSE = [
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
                ],
                "is_active": [
                    "Este campo não pode ser nulo.",
                    "Esse campo precisa ser do tipo boolean."
                ],
            }
        },
        response_only=True,
        status_codes=["400"],        
    ),
    OpenApiExample(
        "Unauthorized/Token not found",
        description='<p>Falha de autenticação, credenciais não informadas.</p>\
        <i>Authentication failed, credentials not assigned.</i>',
        value={
            'message': 'As credenciais de autenticação não foram fornecidas.',
        },
        response_only=True,
        status_codes=["401"],        
    ),
    OpenApiExample(
        "Unauthorized/Token is invalid",
        description='<p>Falha de autenticação, credenciais informadas inválidas.</p>\
        <i>Authentication failed, invalid credentials.</i>',
        value={
            'message': 'As credenciais de autenticação são inválidas.',
        },
        response_only=True,
        status_codes=["401"],        
    ),                                 
]
