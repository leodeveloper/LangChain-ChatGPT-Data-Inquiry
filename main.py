
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_openai import OpenAIEmbeddings
import sys
import os

os.environ["OPENAI_API_KEY"]="sk-YourKey
data=TextLoader("mydata.txt")
prompt=sys.argv[1]
 
index=VectorstoreIndexCreator().from_loaders([data])
response=index.query(prompt)
print(response) 