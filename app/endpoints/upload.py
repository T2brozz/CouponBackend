from datetime import datetime

from fastapi import APIRouter, Depends, File, UploadFile

from app.database import db
from app.models.bill import Bill
from .authentication import UserModel, get_current_active_user
from ..util import uuid

router = APIRouter(tags=["upload"])


@router.post("/new_entry/")
async def upload_entry(category: str, price: float, date: datetime, file: UploadFile = File(...),
                       current_user: UserModel = Depends(get_current_active_user)):
    file_uuid = uuid()
    filename = f"./pictures/{file_uuid}.{file.filename.split('.')[-1]}"
    f = open(filename, "wb")
    file_content = await file.read()
    f.write(file_content)
    f.close()
    db.add(Bill(uuid=file_uuid, filepath=filename, price=price, date=date, category=category, user=current_user.name))
    db.commit()

    return {"filename": file.filename}
