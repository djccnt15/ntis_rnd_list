from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/uid/', response_model=schemas.Uid)
def create_uids(uid: schemas.Uid, db: Session = Depends(get_db)):
    db_uid = crud.get_uid(db, uid_id=uid.id)
    if db_uid:
        raise HTTPException(status_code=400, detail='Uid already registered')
    return crud.create_uid(db=db, uid=uid)


@app.get('/uid/{uid_id}', response_model=schemas.Uid)
def read_uid(uid_id: int, db: Session = Depends(get_db)):
    db_uid = crud.get_uid(db, uid_id=uid_id)
    if db_uid is None:
        raise HTTPException(status_code=404, detail='Uid not found')
    return db_uid


@app.get('/uid/', response_model=list[schemas.Uid])
def read_uids(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    uids = crud.get_uids(db, skip=skip, limit=limit)
    return uids


@app.get('/detail/', response_model=schemas.Detail)
def create_details(uid_id: int, detail: schemas.Detail, db: Session = Depends(get_db)):
    db_detail = crud.get_detail(db, detail_id=detail.id)
    if db_detail:
        raise HTTPException(status_code=400, detail='Uid already registered')
    return crud.create_detail(db=db, detail=detail, uid_id=uid_id)


@app.get('/detail/{detail_id}', response_model=schemas.Detail)
def read_detail(detail_id: int, db: Session = Depends(get_db)):
    db_uid = crud.get_detail(db, detail_id=detail_id)
    if db_uid is None:
        raise HTTPException(status_code=404, detail='Uid not found')
    return db_uid


@app.get('/detail/', response_model=list[schemas.Detail])
def read_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    details = crud.get_details(db, skip=skip, limit=limit)
    return details