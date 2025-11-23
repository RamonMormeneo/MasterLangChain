# embeddings de OpenAI

from langchain_openai import OpenAIEmbeddings

# primero cargamos la API KEY de OpenAI

from dotenv import load_dotenv 
import os

# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# iniciamos modelo, text-embedding-ada-002 por defecto

modelo = OpenAIEmbeddings()

# lista de textos

textos = ['¡Hola!', '¡Oh, hola!', '¿Cómo te llamas?', 'Mis amigos me llaman Mundo', '¡Hola Mundo!']

len(textos)

# embeddings desde una lista de textos

embeddings = modelo.embed_documents(textos)

# nº de vectores

len(embeddings)
# dimensiones de cada vector

len(embeddings[0])

embedding = modelo.embed_query('Hola que tal estas?')

# dimensiones del vector

len(embedding)

#BBDD pip install chroma

from langchain.vectorstores import Chroma

# creacion de la base de datos

db = Chroma.from_texts(texts=textos,                 # lista de textos a guardar
                       embedding=OpenAIEmbeddings(), # funcion de embedding
                       persist_directory= './',      # ruta guardado de la base de datos
                       collection_name='prueba'      # nombre de la coleccion
                      )

# consulta

db.similarity_search(query='hola',   # consulta de usuario 
                     k=3,            # k documentos mas parecidos
                    )