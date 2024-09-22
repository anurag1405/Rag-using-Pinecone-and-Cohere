from fastapi import APIRouter,HTTPException
from models.query import Query
from models.file import TextPayload
from chat_service.agent_service import generate_answer
from utils.pineconedb import add_file_to_vector_store



router = APIRouter()

@router.post("/query")
async def query_endpoint(query: Query):
    result = await generate_answer(query)
    return result

@router.post("/uploadfile")
async def upload_file_endpoint(payload: TextPayload):
    text = payload.text
    if text:
        result = add_file_to_vector_store(text)
        return result
    else:
        raise HTTPException(status_code=400, detail="No text provided.")