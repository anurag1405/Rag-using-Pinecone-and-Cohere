from pydantic import BaseModel

class TextPayload(BaseModel):
    text: str