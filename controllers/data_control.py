import openai

class DataControl:

    @classmethod
    def talk_to_gpt(cls, data):
        print(data)

        openai.api_key = 'sua_chave_api_aqui'
        
        try:
            # Fazendo a requisição para o modelo da OpenAI (substitua "text-davinci-003" pelo modelo desejado)
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=data,
                temperature=0.7,
                max_tokens=150,
                n=1,
                stop=None
            )
            # Extraindo o texto da resposta
            answer = response.choices[0].text.strip()
            print(answer)
            return answer
        except Exception as e:
            print(f"Ocorreu um erro ao se comunicar com a API da OpenAI: {e}")
            return "Desculpe, não consegui processar sua pergunta."
    
    
