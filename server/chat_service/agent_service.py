from config import cohere_client
from utils.pineconedb import query_pinecone


async def generate_answer(user_query):
    retrieved_chunks = query_pinecone(user_query)
    context = " ".join(retrieved_chunks)
    PROMPT_TEMPLATE = """
                Answer the question based only on the following context:
                {context}
                Answer the question based on the above context: {user_query}.
                Provide a detailed answer.
                Don’t justify your answers.
                Don’t give information not mentioned in the CONTEXT INFORMATION.
                Do not say "according to the context" or "mentioned in the context" or similar.
    """
    prompt_text = PROMPT_TEMPLATE.format(context=context, user_query=user_query)
    response = cohere_client.generate(
        model='command', 
        prompt=prompt_text, 
        max_tokens=100
    )
    return {'result':response.generations[0].text.strip(),'segments':retrieved_chunks}



