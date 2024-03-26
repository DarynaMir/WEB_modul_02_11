from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import Session

from src.database.db import get_db

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/")
async def get_todos():
    pass

@router.get("/{todo_id}")
async def get_todo():
    pass

@router.post("/")
async def create_todo():
    pass

@router.put("/{todo_id}")
async def update_todo():
    pass

@router.delete("/{todo_id}")
async def delete_todo():
    pass

@app.get("/api/healthchecker")
async def healthchecker(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database error")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connection to Database")

