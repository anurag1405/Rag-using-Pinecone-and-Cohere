from config import pc,cohere_client,index
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document


def generate_embeddings(chunks):
    embeddings = cohere_client.embed(texts=chunks).embeddings
    return embeddings

def upsert_to_pinecone(chunks, embeddings):
    upsert_data = [(f'chunk-{i}', embeddings[i], {'text': chunks[i]}) for i in range(len(chunks))]
    index.upsert(upsert_data)

def query_pinecone(query):
    query_embedding = cohere_client.embed(texts=[query.query]).embeddings
    results = index.query(
        vector=query_embedding[0],  
        top_k=5,                 
        include_metadata=True    
    )
    retrieved_chunks = [match['metadata']['text'] for match in results['matches']]
    return retrieved_chunks


def add_file_to_vector_store(text):
    documents = [Document(page_content=text)]  # Wrap text in Document
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)  # Use the Document object
    chunk_texts = [chunk.page_content for chunk in chunks]
    embed = generate_embeddings(chunk_texts)
    upsert_to_pinecone(chunk_texts, embed)
    return {'message':'success'}
