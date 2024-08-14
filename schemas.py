from pydantic import BaseModel
from uuid import UUID

# Modelo base para os dados do usuário, contendo campos comuns a todas as operações relacionadas ao usuário
class UserBase(BaseModel):
    nome_completo: str  # Nome completo do usuário
    idade: int  # Idade do usuário
    nota_primeiro_semestre: float  # Nota do primeiro semestre do usuário
    nota_segundo_semestre: float  # Nota do segundo semestre do usuário
    nome_professor: str  # Nome do professor associado ao usuário
    numero_sala: int  # Número da sala associada ao usuário

# Modelo utilizado ao criar um novo usuário. Herda todos os campos de UserBase.
class UserCreate(UserBase):
    pass  # Nenhum campo adicional é necessário para a criação, então apenas herda de UserBase

# Modelo utilizado ao atualizar um usuário existente. Herda todos os campos de UserBase.
class UserUpdate(UserBase):
    pass  # Nenhum campo adicional é necessário para a atualização, então apenas herda de UserBase

# Modelo utilizado para retornar dados do usuário nas respostas da API. Herda todos os campos de UserBase.
class UserResponse(UserBase):
    id: UUID  # Identificador único para o usuário

    class Config:
        orm_mode = True  # Configuração que informa ao Pydantic para ler dados como objetos em vez de dicionários