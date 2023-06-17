from drf_spectacular.utils import OpenApiExample

REQUESTS_POST = {
    "application/json": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Nome resumido para o setor de internação", "required": True, "max_lengh": 15},
            "description": {"type": "string", "description": "Descrição do setor de internação", "required": True, "max_lengh": 145},
            "tip_acc": {"type": "string", "description": "Tipo de acomodação que caracteriza o setor de internação", "required": True},
            "is_active": {"type": "boolean", "description": "Setor de internação será criado como ativo ou não", "required": False, "default": True}
        }
    }            
}

RESPONSE_POST = [
    OpenApiExample(
        "Success",
        description='<p>Sucesso ao cadastrar um novo Setor.</p>\
        <i>Success in registering a new sector.</i>',
        value={
            'message': 'Setor cadastrado.',
            'data': [
                {
                    "id": 0,
                    "name": "string",
                    "description": "string",
                    "tip_acc": "string",
                    "activation_date": "string",
                    "deactivation_date": "string",
                    "is_active": True
                }
            ]
        },
        response_only=True,
        status_codes=["201"],        
    ),
    OpenApiExample(
        "Bad Request",
        description='<p>Falha ao cadastrar o setor de internação, verifique os dados inseridos e tente novamente.</p>\
        <i>Failed to register the hospitalization sector, check the entered data and try again.</i>',
        value={
            'message': 'Falha ao cadastrar o setor de internação, verifique os dados inseridos e tente novamente.',
            'data': {
                "name": [
                    "Este campo é obrigatório.",
                    "Este campo não pode ser nulo.",
                    "Este campo não pode ser em branco.",
                    "Setor com este Nome já existe."
                ],
                "description": [
                    "Este campo é obrigatório.",
                    "Este campo não pode ser nulo.",
                    "Este campo não pode ser em branco.",
                    "Setor com esta Descrição já existe."
                ],
                "tip_acc": [
                    "Este campo é obrigatório.",
                    "Este campo não pode ser nulo.",
                    "Este campo não pode ser em branco.",
                    "Tipo de acomodação inválido."
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
    OpenApiExample(
        "Not found",
        description='<p>Hospital não encontrado ou não informado.</p>\
        <i>Hospital not found or not informed.</i>',
        value={
            'message': 'Hospital não encontrado ou não informado.',
        },
        response_only=True,
        status_codes=["404"],        
    ),
]