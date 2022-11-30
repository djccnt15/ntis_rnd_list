from datetime import date

from pydantic import BaseModel


class Uid(BaseModel):
    """record for uid of rnd list"""

    id: int
    serial: int
    uid: int

    class Config:
        orm_mode = True


class Detail(BaseModel):
    """record for detail information of R&D"""

    id: int
    uid_id: int
    title: str
    department: str
    gov_agency: str
    date_notice: date
    budget: str

    class Config:
        orm_mode = True


class KeyWord(BaseModel):
    """record for keyword of title"""

    id: int
    detail_id: int
    keyword: str