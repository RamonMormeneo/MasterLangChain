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

from langchain.utilities import SQLDatabase

from langchain.schema.runnable import RunnablePassthrough

# iniciamos el modelo de OpenAI

modelo = ChatOpenAI()

# parser de salida, transforma la salida a string

parser = StrOutputParser()

# definimos el primer prompt

plantilla_sql = '''Basado en el esquema de la tabla a continuación, escribe una consulta SQL 
                   que responda a la pregunta del usuario:
              
                   {esquema}
              
                   Pregunta: {pregunta}
              
                   Query SQL:'''


prompt_sql = ChatPromptTemplate.from_template(plantilla_sql)

# conexion a la base de datos mysql

uri = 'mysql+pymysql://root:password@localhost:3306/publications'

db = SQLDatabase.from_uri(uri)

# descripcion de la base de datos

db.get_table_info()[:300].split('\n')

# cadena creadora de queries

cadena_sql = (RunnablePassthrough.assign(esquema=lambda _: db.get_table_info())
              
              | prompt_sql
              
              | modelo.bind(stop=["\nSQLResult:"])
              
              | parser
             
             )

# respuesta de la cadena sql

respuesta_sql = cadena_sql.invoke({'pregunta': '¿cuantos empleados hay?'})

respuesta_sql

# ejecucion de la query

db.run(respuesta_sql)

# definimos el segundo prompt

plantilla = '''Basado en el esquema de la tabla a continuación, 
               la pregunta, la consulta SQL y la respuesta SQL, 
               escribe una respuesta en lenguaje natural:
               
               {esquema}

               Pregunta: {pregunta}
               Query SQL: {query}
               Respuesta SQL: {respuesta}'''


prompt = ChatPromptTemplate.from_template(plantilla)

# cadena completa

cadena = (RunnablePassthrough.assign(query=cadena_sql)
          
          | RunnablePassthrough.assign(esquema=lambda _: db.get_table_info(),
                                       respuesta=lambda x: db.run(x['query']))
          
          | prompt
          
          | modelo
          
          | parser
         
         )

# respuesta de la cadena completa

cadena.invoke({'pregunta': '¿cuantos empleados hay?'})