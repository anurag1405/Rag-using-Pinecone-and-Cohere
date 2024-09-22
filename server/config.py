import os
from dotenv import load_dotenv
import cohere
from pinecone import Pinecone, ServerlessSpec
import time

load_dotenv()
pine = os.getenv("PINECONE")
co = os.getenv('COHERE')
pc = Pinecone(api_key=pine)
cohere_client = cohere.Client(co)

index_name='cohere'
if index_name in pc.list_indexes().names():
        pc.delete_index(index_name)

pc.create_index(
    name=index_name,
    dimension=4096,
    metric="cosine", 
    spec=ServerlessSpec(
    cloud="aws",
    region="us-east-1"
    ) 
)
while not pc.describe_index(index_name).status['ready']:
    time.sleep(1)
index= pc.Index(index_name)