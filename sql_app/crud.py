from datetime import datetime

from sqlalchemy.orm import Session

from . import models, schemas


def get_uid(db: Session, uid_id: int):
    return db.query(models.Uid).filter(models.Uid.id == uid_id).first()


def get_uids(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Uid).offset(skip).limit(limit).all()


def create_uid(db: Session, uid: schemas.Uid):
    db_uid = models.Uid(serial=uid.serial, uid=uid.uid)
    db.add(db_uid)
    db.commit()
    db.refresh(db_uid)
    return db_uid


def get_detail(db: Session, detail_id: int):
    return db.query(models.Detail).filter(models.Detail.id == detail_id).first()


def get_details(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Detail).offset(skip).limit(limit).all()


def create_detail(db: Session, detail: schemas.Detail, uid_id: int):
    db_detail = models.Detail(**detail.dict(), uid_id=uid_id)
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail


def get_keyword(db: Session, keyword_id: int):
    return db.query(models.KeyWord).filter(models.KeyWord.id == keyword_id).first()


def get_keywords(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.KeyWord).offset(skip).limit(limit).all()


def create_keyword(db: Session, detail: schemas.KeyWord, detail_id: int):
    db_detail = models.Detail(**detail.dict(), detail_id=detail_id)
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail


def get_log_scrap(db: Session, date_scrap: datetime):
    return db.query(models.LogScrap).filter(models.LogScrap.date_scrap == date_scrap).first()


def get_logs_scrap(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LogScrap).offset(skip).limit(limit).all()


def create_log_scrap(db: Session, date_scrap: schemas.LogScrap):
    db_date_scrap = models.LogScrap(date_scrap=date_scrap.date_scrap)
    db.add(db_date_scrap)
    db.commit()
    db.refresh(db_date_scrap)
    return db_date_scrap