# primero cargamos la API KEY de OpenAI

from dotenv import load_dotenv 
import os

# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# librerias

from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# importamos un archivo de texto

with open('../../../files/state_of_the_union.txt', 'r') as f:
    
    texto = f.read()

# usamos el splitter

splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

# troceamos el texto

trozos = splitter.split_text(texto)

len(trozos)

# modelo de embedding

modelo = OpenAIEmbeddings()

# creacion de la base de datos

db = Chroma.from_texts(texts=trozos, 
                       embedding=OpenAIEmbeddings(), 
                       persist_directory= './db', 
                       collection_name='estado')

# definicion de recuperador

recuperador = db.as_retriever()

# consulta del usuario

consulta = 'What did the president say about Ketanji Brown Jackson?'

# recuperar documentos

docs = recuperador.invoke(consulta)

# 4 documentos por defecto

len(docs)

# contenido del primer documento, el mas parecido a nuestra consulta

docs[0].page_content

from langchain_openai import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever

llm = ChatOpenAI(temperature=0)

recuperador =  MultiQueryRetriever.from_llm(retriever=db.as_retriever(), 
                                            llm=llm)

consulta2 = 'What are the approaches to Task Decomposition?'

docs = recuperador.invoke(consulta2)

len(docs)

from langchain_openai import OpenAI
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

llm = OpenAI(temperature=0)

compresor = LLMChainExtractor.from_llm(llm)

recuperador = ContextualCompressionRetriever(base_compressor=compresor, 
                                             base_retriever=db.as_retriever())

docs = recuperador.get_relevant_documents(consulta)

len(docs)

docs[0].page_content

#ensamble retriver
from langchain.retrievers import BM25Retriever, EnsembleRetriever

# recuperador BM25

recuperador_bm25 = BM25Retriever.from_texts(trozos)

# ensamblaje de recuperadores con el mismo peso

recuperador_ensamblado = EnsembleRetriever(retrievers=[recuperador_bm25, db.as_retriever()], 
                                           weights=[0.5, 0.5])

docs = recuperador_ensamblado.get_relevant_documents(consulta)

docs[0].page_content