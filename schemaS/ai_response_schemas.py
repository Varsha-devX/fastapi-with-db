from pydantic import BaseModel
from typing import Any, Optional

class AIRequest(BaseModel):
    message: str
    system_prompt: Optional[str] = "You are a helpful assistant."

class AIResponse(BaseModel):
    response: Any