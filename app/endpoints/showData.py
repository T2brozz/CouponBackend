from datetime import datetime

from fastapi import APIRouter, Depends

from app.database import db
from app.models.bill import Bill
from .authentication import UserModel, get_current_active_user
from ..util import uuid

router = APIRouter(tags=["getData"])


@router.get("/get_list")
async def get_list(start_date: datetime, end_date: datetime,
                   current_user: UserModel = Depends(get_current_active_user)):
    query = db.query(Bill).filter(Bill.date.between(start_date, end_date)).all()
    print(query)
    return {"list": query}
