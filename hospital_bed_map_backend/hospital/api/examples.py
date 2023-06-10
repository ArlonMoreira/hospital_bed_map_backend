from drf_spectacular.utils import OpenApiExample

REQUESTS = {
    "application/json": {
        "type": "object",
        "properties": {
            "cnes": {"type": "number", "description": "cnes", "required": True},
            "cnpj": {"type": "number", "description": "cnpj", "required": True},
            "name": {"type": "string", "description": "Nome completo do hospital", "required": True, "min_lengh": 10, "max_lengh": 255},
            "acronym": {"type": "string", "description": "Sigla do hospital", "required": True, "max_lengh": 45},
            "is_active": {"type": "boolean", "description": "Hospital será criado como ativo ou não", "required": False, "default": True}
        }
    }            
}

RESPONSE_GET = [
    OpenApiExample(
        "Success",
        description='<p>Pode retornar um ou mais hospitais de acordo com id passado na URL da requisição.</p>\
        <i>It can return one or more hospitals according to the id passed in the request URL.</i>',
        value={
            'message': 'Dados obtidos com sucesso.',
            'data': [
                {
                    "id": 0,
                    "cnes": "string",
                    "cnpj": "string",
                    "name": "string",
                    "acronym": "string",
                    "is_active": True
                }                
            ]
        },
        response_only=True,
        status_codes=["200"],        
    ),    
    OpenApiExample(
        "Not found",
        description='<p>Falha ao encontrar o hospital, pois o ID informado não existe no banco de dados.</p>\
        <i>Failed to find the hospital, as the ID entered does not exist in the database.</i>',
        value={
            'message': 'Hospital {id} não encontrado.',
        },
        response_only=True,
        status_codes=["404"],        
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

RESPONSE_PUT = [
    OpenApiExample(
        "Success",
        description='<p>Sucesso ao atualizar os dados de um hospital.</p>\
        <i>Success in updating hospital data.</i>',
        value={
            'message': 'Dados do hospital atualizado.',
            'data': [
                {
                    "id": 0,
                    "cnes": "string",
                    "cnpj": "string",
                    "name": "string",
                    "acronym": "string",
                    "is_active": True
                }                        
            ]
        },
        response_only=True,
        status_codes=["200"],        
    ),
    OpenApiExample(
        "Bad Request",
        description='<p>Falha ao atualizar hospital pois os parâmetros informados não estão conforme o esperado.</p>\
        <i>Failed to update hospital because the parameters entered are not as expected.</i>',
        value={
            'message': 'Falha ao atualizar hospital, verifique os dados inseridos e tente novamente.',
            'data': {
                "cnes": [
                    "Este campo é obrigatório.",
                    "Este campo não pode ser em branco.",
                    "Hospital com este cnes já existe.",
                    "Um número inteiro válido é exigido."
                ],
                "cnpj": [
                    "Este campo é obrigatório.",
                    "Este campo não pode ser em branco.",
                    "Hospital com este cnpj já existe.",
                    "CNPJ inválido",
                    "Certifique-se de que este campo não tenha mais de 14 caracteres."
                ],
                "acronym": [
                    "Este campo é obrigatório.",
                    "Este campo não pode ser em branco.",
                    "Hospital com este Sigla já existe.",
                    "Este campo não pode ser nulo.",
                    "Este campo não pode ser em branco.",
                ],                
                "name": [
                    "Este campo é obrigatório.",
                    "Este campo não pode ser em branco.",
                    "Hospital com este Nome já existe.",
                    "Este campo não pode ser nulo.",
                    "Este campo não pode ser em branco.",
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

RESPONSE_POST = [
    OpenApiExample(
        "Success",
        description='<p>Sucesso ao cadastrar um novo hospital.</p>\
        <i>Success in registering a new hospital.</i>',
        value={
            'message': 'Hospital cadastrado.',
            'data': [
                {
                    "id": 0,
                    "cnes": "string",
                    "cnpj": "string",
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
                "cnes": [
                    "Este campo é obrigatório.",
                    "Este campo não pode ser em branco.",
                    "Hospital com este cnes já existe.",
                    "Um número inteiro válido é exigido."
                ],
                "cnpj": [
                    "Este campo é obrigatório.",
                    "Este campo não pode ser em branco.",
                    "Hospital com este cnpj já existe.",
                    "CNPJ inválido",
                    "Certifique-se de que este campo não tenha mais de 14 caracteres."
                ],
                "acronym": [
                    "Este campo é obrigatório.",
                    "Este campo não pode ser em branco.",
                    "Hospital com este Sigla já existe.",
                    "Este campo não pode ser nulo.",
                    "Este campo não pode ser em branco.",
                ],                
                "name": [
                    "Este campo é obrigatório.",
                    "Este campo não pode ser em branco.",
                    "Hospital com este Nome já existe.",
                    "Este campo não pode ser nulo.",
                    "Este campo não pode ser em branco.",
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
