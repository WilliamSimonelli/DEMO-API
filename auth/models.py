# auth/models.py
from pydantic import BaseModel

class User(BaseModel):
    username: str
    disabled: bool = None

class UserInDB(User):
    hashed_password: str

# Usuário fictício para demonstração
fake_user_db = {
    "johndoe": {
        "username": "william",
        "full_name": "william simonelli",
        "email": "williamsimonelli09@gmail.com",
        "hashed_password": "$2b$12$eImGu9qzHjJ9R0d.4G8HeObJLptZrk8b8bE/dbIt6LJQRezypThq2",
        "disabled": False,
    }
}


# Pode ser adicionada em models.py ou diretamente em routes.py
def get_user(fake_db, username: str):
    if username in fake_user_db:
        user_dict = fake_user_db[username]
        return UserInDB(**user_dict)
    return None

