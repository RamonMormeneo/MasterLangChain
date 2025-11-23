# cargamos la API KEY de OpenAI

from dotenv import load_dotenv 
import os

# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# importamos librerias

from langchain_openai import ChatOpenAI

from langchain_openai import OpenAIEmbeddings

from langchain.prompts import PromptTemplate

from langchain.schema.output_parser import StrOutputParser

from langchain.schema.runnable import RunnableLambda

from langchain.utils.math import cosine_similarity

# iniciamos el modelo de OpenAI

modelo = ChatOpenAI()

# parser de salida, transforma la salida a string

parser = StrOutputParser()

# definimos el primer prompt

plantilla_fisica = '''Eres un profesor de física muy inteligente.
                      Eres excelente respondiendo preguntas sobre física de 
                      manera concisa y fácil de entender.
                      Cuando no sabes la respuesta a una pregunta, admites que no la sabes.
                      
                      Aquí tienes una pregunta:
                      {pregunta}
                      
                    '''

# definimos el segundo prompt

plantilla_matematicas = '''Eres un muy buen matemático. 
                           Eres excelente respondiendo preguntas de matemáticas.
                           Eres tan bueno porque puedes descomponer problemas difíciles 
                           en sus partes componentes, responder esas partes y 
                           luego juntarlas para responder la pregunta más amplia.
                           
                           Aquí tienes una pregunta:
                           {pregunta}
                        '''

# los ponemos en una lista para usarlos despues

plantillas = [plantilla_fisica, plantilla_matematicas]

# iniciamos el modelo de embedding

modelo_embeddings = OpenAIEmbeddings()

# realizamos la vectorizacion de los prompts

prompt_embeddings = modelo_embeddings.embed_documents(plantillas)

# longitud del vector de embedding

len(prompt_embeddings[0])

# funcion para enrutar el prompt

def enrutador_prompt(usuario: dict) -> PromptTemplate.from_template:
    
    """
    Esta función decide el comportamiento del modelo segun 
    la pregunta del usuario. Compara la similitud entre la pregunta realizada
    y los prompts de matematicas o fisica y decide cual de ellos usar.
    
    Params:
    usuario: dict, diccionario con la key 'pregunta'
    
    Return:
    objeto PromptTemplate.from_template para ser pasado a la cadena
    """
    
    global modelo_embeddings, prompt_embeddings, plantillas

    embedding_pregunta = modelo_embeddings.embed_query(usuario['pregunta'])
    
    similitud = cosine_similarity([embedding_pregunta], prompt_embeddings)[0]
    
    mas_similar = plantillas[similitud.argmax()]
    
    print('Usando MATEMATICAS' if mas_similar == plantilla_matematicas else 'Usando FISICA')
    
    return PromptTemplate.from_template(mas_similar)

# creamos la cadena

cadena = RunnableLambda(enrutador_prompt) | modelo | parser

# respuesta de la cadena

cadena.invoke({'pregunta': 'qué es un agujero negro'})

# respuesta de la cadena

cadena.invoke({'pregunta': 'qué es una integral de caminos'})