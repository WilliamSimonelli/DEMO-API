from fastapi import APIRouter, Body, Depends
from models.base_models import stringToRecieve, Message
from controllers.data_control import DataControl
from auth.dependencies import get_current_user
from auth.models import UserInDB

api_sample = APIRouter()


#proteger: current_user: UserInDB = Depends(get_current_user)

@api_sample.get("/alexa",
                response_model=str, 
                tags=["Alexa Endpoints"], 
                summary="Obter perguntas realizadas",
                description="Recebe o histórico de perguntas realizadas.")
async def get_latest_questions():
    try:
        return "Pinolino boiola"
    except Exception as e:
        print(f"Ocorreu algum erro: {str(e)}")
        return {str(e)}


@api_sample.get("/get_messege",
                response_model=str, 
                tags=["Mensagens"], 
                summary="Obter perguntas realizadas",
                description="Recebe o histórico de perguntas realizadas.")
async def get_latest_questions():
    try:
        return "retorna correto??"
    except Exception as e:
        print(f"Ocorreu algum erro: {str(e)}")
        return {str(e)}



@api_sample.post("/post_question",
                response_model=str, 
                tags=["Mensagens"], 
                summary="Enviar perguntas",
                description="Envie uma pergunta aqui e receba uma resposta.")
async def read_questions(
    data: stringToRecieve = Body(...)
):
    try:
        print("mensagem recebida no post: " + str(data.mensagem))
        res =  await DataControl.talk_to_gpt(data=data)
        return res
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
        return str(e)
    
    
