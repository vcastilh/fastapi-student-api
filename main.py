from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from models import User as UserModel
from database import SessionLocal, create_tables
from schemas import UserResponse, UserCreate, UserUpdate

app = FastAPI(
    title="Student Management API",
    description="This API allows you to perform CRUD operations on user data, including creating, reading, updating, and deleting users.",
    version="1.0.0"
)

# Garantir que as tabelas sejam criadas no início
create_tables()

# Dependência para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db  # Retorna a sessão do banco de dados para uso
    finally:
        db.close()  # Garante que a sessão seja fechada após o uso

# Rota raiz, geralmente usada para verificar se a API está funcionando
@app.get("/")
async def root():
    return {
        "mensagem": "Bem-vindo à API RESTful",
        "descrição": "Esta API foi construída utilizando FastAPI, SQLAlchemy e PostgreSQL, com deploy no Render.",
        "versão": "1.0.0",
        "tecnologias": {
        "framework": "FastAPI",
        "banco de dados": " PostgreSQL com SQLAlchemy ORM",
        "deploy": "Render",
        "linguagem": "Python 3.11",
        "outros": "Pydantic para validação de dados, Uvicorn como servidor ASGI"
  },
  "documentação_url": "/docs",
  "contato": "viniciaofelix@gmail.com"
    }

# Endpoint para buscar todos os usuários no banco de dados
@app.get('/api/v1/users', response_model=List[UserResponse], status_code=status.HTTP_200_OK)
async def fetch_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()  # Consulta todos os usuários no banco de dados
    return users  # Retorna a lista de usuários

# Endpoint para buscar um usuário específico pelo ID
@app.get('/api/v1/users/{user_id}', response_model=UserResponse, status_code=status.HTTP_200_OK)
async def fetch_user_id(user_id: str, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()  # Busca o usuário pelo ID
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID: {user_id} não existe")
    return user  # Retorna os dados do usuário se encontrado

# Endpoint para criar um novo usuário
@app.post("/api/v1/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Cria um novo objeto UserModel com os dados recebidos
    db_user = UserModel(
        nome_completo=user.nome_completo,
        idade=user.idade,
        nota_primeiro_semestre=user.nota_primeiro_semestre,
        nota_segundo_semestre=user.nota_segundo_semestre,
        nome_professor=user.nome_professor,
        numero_sala=user.numero_sala
    )
    db.add(db_user)  # Adiciona o novo usuário ao banco de dados
    db.commit()  # Confirma as alterações no banco de dados
    db.refresh(db_user)  # Atualiza o objeto db_user com os dados do banco de dados
    return db_user  # Retorna os dados do usuário recém-criado

# Endpoint para atualizar um usuário existente
@app.put('/api/v1/users/{user_id}', response_model=UserResponse, status_code=status.HTTP_200_OK)
async def update_user(user_id: str, updated_user: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()  # Busca o usuário pelo ID
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID: {user_id} não existe")
    
    # Atualiza os campos do usuário com os dados recebidos
    user.nome_completo = updated_user.nome_completo
    user.idade = updated_user.idade
    user.nota_primeiro_semestre = updated_user.nota_primeiro_semestre
    user.nota_segundo_semestre = updated_user.nota_segundo_semestre
    user.nome_professor = updated_user.nome_professor
    user.numero_sala = updated_user.numero_sala
    db.commit()  # Confirma as alterações no banco de dados
    db.refresh(user)  # Atualiza o objeto user com os dados do banco de dados
    return user  # Retorna os dados do usuário atualizado

# Endpoint para deletar um usuário pelo ID
@app.delete("/api/v1/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()  # Busca o usuário pelo ID
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID: {user_id} não existe")
    db.delete(user)  # Remove o usuário do banco de dados
    db.commit()  # Confirma as alterações no banco de dados
    return  # Retorna uma resposta vazia com status 204 (No Content)