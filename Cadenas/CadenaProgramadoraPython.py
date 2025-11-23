# cargamos la API KEY de OpenAI

from dotenv import load_dotenv 
import os

# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# importamos librerias

from langchain_openai import ChatOpenAI

from langchain.prompts import ChatPromptTemplate

from langchain.schema.output_parser import StrOutputParser

from langchain_experimental.utilities import PythonREPL
# iniciamos el modelo de OpenAI

modelo = ChatOpenAI()

# parser de salida, transforma la salida a string

parser = StrOutputParser()

# definimos el prompt

plantilla = '''Write some python code to solve the user's problem.
               
               Return only python code in Markdown format, e.g.:

               ```python
               ....
               ```
               '''


prompt = ChatPromptTemplate.from_messages([('system', plantilla), ('human', '{pregunta}')])

# cambio de la string de salida

def limpiar_salida(texto: str) -> str:
    """
    Esta funcion limpia la salida del modelo.
    El modelo devolvera markdown y esta funcion 
    devolvera el codigo en formato string
    
    Params:
    texto: str, formato markdown
    
    Return:
    codigo en formato string
    """
    
    texto = texto.split('```python')[1].replace('```', '')
    
    return texto

# definicion de la cadena

cadena = prompt | modelo | parser | limpiar_salida | PythonREPL().run

# respuesta de la cadena

respuesta = cadena.invoke({'pregunta' :'cuanto es 2 y 2'})

print(respuesta)

# respuesta de la cadena

respuesta = cadena.invoke({'pregunta' :'8 factorial'})

print(respuesta)