#pipi install langServe[all]
#Es necesario crear un servidor en langserve el codigo en el servidor seria el siguiente por ejemplo

# librerias

from dotenv import load_dotenv 
import os

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from fastapi import FastAPI
import uvicorn
from langserve import add_routes



# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')



# creacion de la aplicacion de FastAPI
app = FastAPI(title='Servidor LangChain', 
              version='1.0',
              description='Simple API con LangChain')


# inicio del modelo
modelo = ChatOpenAI()


# creacion del prompt
plantilla = 'Eres un asistente personal que responde la siguiente pregunta de la mejor manera: {pregunta}'

prompt = ChatPromptTemplate.from_template(plantilla)


# se define la cadena
cadena = prompt | modelo

# se añade el endpoint a la aplicacion
add_routes(app, cadena, path='/cadena')


# ejecucion de la API
if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
  
#  una vez levantado se puede usar el servidor desde el navegador con la siguiente url http://localhost:8000/cadena/playground/

#curl --location --request POST 'http://localhost:8000/cadena/invoke/' \ --header 'Content-Type: application/json' \ --data-raw '{"input": {"pregunta": "hola"}}'

#para conectar desde python

import requests as req

endpoint = 'http://localhost:8000/cadena/invoke/'

pregunta = 'hola'

respuesta = req.post(endpoint, json={'input': {'pregunta': pregunta}})

respuesta.json()

# respuesta formato string

respuesta.json()['output']['content']