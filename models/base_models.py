
from pydantic import BaseModel, Field

class stringToRecieve(BaseModel, extra='forbid'):
    mensagem: str = Field(..., min_length=1)


class Message(BaseModel):
    primeira_rota: str