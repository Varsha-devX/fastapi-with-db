from pydantic import BaseModel
from typing import Any, Optional

class AIRequest(BaseModel):
    message: str
    system_prompt: Optional[str] = "You are a helpful assistant."
    user_id: Optional[int] = None

class AIResponse(BaseModel):
    response: Any

class ChatMessageSchema(BaseModel):
    role: str
    content: str
    timestamp: Optional[str] = None

    class Config:
        from_attributes = True

class ChatHistoryResponse(BaseModel):
    messages: list[ChatMessageSchema]
