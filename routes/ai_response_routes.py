from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import ChatMessage
from utils.ai_response import get_completion
from schemaS.ai_response_schemas import AIRequest, AIResponse, ChatHistoryResponse
from datetime import datetime

router = APIRouter()


@router.post("/ask", response_model=AIResponse)
def ask_ai(request: AIRequest, db: Session = Depends(get_db)):
    """Get response from AI model and save to history if user_id is provided."""
    try:
        response_content = get_completion(request.message, request.system_prompt)
        
        if request.user_id:
            # Save user message
            user_msg = ChatMessage(
                user_id=request.user_id,
                role="user",
                content=request.message,
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            db.add(user_msg)
            
            # Save assistant message
            assistant_msg = ChatMessage(
                user_id=request.user_id,
                role="assistant",
                content=response_content,
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            db.add(assistant_msg)
            db.commit()

        return AIResponse(response=response_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history/{user_id}", response_model=ChatHistoryResponse)
def get_history(user_id: int, db: Session = Depends(get_db)):
    """Retrieve chat history for a specific user."""
    messages = db.query(ChatMessage).filter(ChatMessage.user_id == user_id).order_by(ChatMessage.id.asc()).all()
    return ChatHistoryResponse(messages=messages)