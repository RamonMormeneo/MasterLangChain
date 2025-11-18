# primero cargamos la API KEY de OpenAI

from dotenv import load_dotenv 
import os

# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# importamos llm desde LangChain

from langchain_openai import OpenAI

# iniciamos el llm, por defecto gpt-3.5-turbo-instruct

llm = OpenAI() 

# uso del llm con el metodo invoke

llm.invoke('hola como estas?')
# otro ejemplo

respuesta = llm.invoke('¿cuales son las 7 maravillas del mundo?')

print(respuesta)

for chunk in llm.stream('¿cuales son las 7 maravillas del mundo?'):
    
    print(chunk, end='', flush=True)

#modelos de chat

# importamos el modelo de chat de OpenAI

from langchain_openai import ChatOpenAI

# iniciamos el chat, por defecto gpt-3.5-turbo

chat = ChatOpenAI()

# uso del chat con string

chat.invoke('hola')

# cambio a gpt-4o

chat = ChatOpenAI(model_name='gpt-4o')

# uso del chat con string

chat.invoke('hola')

from langchain.schema.messages import HumanMessage, SystemMessage


mensajes = [SystemMessage(content='Eres Micheal Jordan.'),
            HumanMessage(content='¿Con qué fabricante de zapatos estás asociado?')]


respuesta = chat.invoke(mensajes)


respuesta

# string de respuesta

print (respuesta.content)

#pprompts

# importamos la plantilla de prompts

from langchain.prompts import PromptTemplate

# definimos la plantilla

plantilla = PromptTemplate.from_template('Cuentame un chiste {adjetivo} sobre {contenido}.')

# variables de usuario

adjetivo = 'gracioso'

contenido = 'robots'

# definimos el prompt completo

prompt = plantilla.format(adjetivo=adjetivo, contenido=contenido)

# uso del prompt en el chat

chat.invoke(prompt).content

# importamos la plantilla de prompts para chats

from langchain.prompts import ChatPromptTemplate

# definimos un prompt de chat para varios roles

plantilla_chat = ChatPromptTemplate.from_messages([
    
    ('system', 'Eres un buen asistente personal. Tu nombre es {nombre}.'),
    ('human', 'Hola, ¿como estas?'),
    ('ai', 'Estoy bien, gracias.'),
    ('human', '{pregunta}')

])

# formateo del mensaje

mensajes = plantilla_chat.format_messages(nombre='Pepe', pregunta='¿Como te llamas?')


for m in mensajes:
    print(m)

chat.invoke(mensajes).content

#parsers de slaida

from langchain.output_parsers.json import SimpleJsonOutputParser

# creamos un prompt pidiendole un JSON 

json_prompt = PromptTemplate.from_template(
    'Devuelve un JSON con `fecha_nacimiento` y `lugar_nacimiento` para la siguiente pregunta: {pregunta}'
)

# iniciamos el parser

json_parser = SimpleJsonOutputParser()

# creamos una cadena con el prompt, modelo y parser

json_chain = json_prompt | chat | json_parser

# llamada a la cadena

json = json_chain.invoke({'pregunta': 'Donde y cuando nacio Elon Musk'})

print(json)

type(json)

from langchain.output_parsers import CommaSeparatedListOutputParser

# iniciamos el parser

parser = CommaSeparatedListOutputParser()

# generamos un prompt

prompt = PromptTemplate.from_template(
    'Devuelve 5 {pregunta}. La respuesta debe ser una lista de strings separadas por coma.'
)

chain = prompt | chat | parser

res = chain.invoke({'pregunta': 'Equipos de la liga española'})

print(res)

type(res)

from langchain.output_parsers import DatetimeOutputParser

# inicamos el parser

parser = DatetimeOutputParser()

prompt = PromptTemplate.from_template(
    'Responde la siguiente pregunta {pregunta}. Devuelve solamente el formato %Y-%m-%dT%H:%M:%S.%fZ.'
)

chain = prompt | chat | parser

chain.invoke({'pregunta': 'Cuando llego el hombre a la luna'})