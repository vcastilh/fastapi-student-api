from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import declarative_base
from uuid import uuid4

# Cria uma classe base para todas as classes de modelo
Base = declarative_base()

# Define o modelo User, que representa a tabela 'users' no banco de dados
class User(Base):
    __tablename__ = 'users'  # Nome da tabela no banco de dados

    # Coluna 'id' que armazena um identificador único para cada usuário
    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))

    # Coluna 'nome_completo' que armazena o nome completo do usuário
    nome_completo = Column(String(255), nullable=False)

    # Coluna 'idade' que armazena a idade do usuário
    idade = Column(Integer, nullable=False)

    # Coluna 'nota_primeiro_semestre' que armazena a nota do usuário no primeiro semestre
    nota_primeiro_semestre = Column(Float, nullable=False)

    # Coluna 'nota_segundo_semestre' que armazena a nota do usuário no segundo semestre
    nota_segundo_semestre = Column(Float, nullable=False)

    # Coluna 'nome_professor' que armazena o nome do professor associado ao usuário
    nome_professor = Column(String(255), nullable=False)

    # Coluna 'numero_sala' que armazena o número da sala associada ao usuário
    numero_sala = Column(Integer, nullable=False)
