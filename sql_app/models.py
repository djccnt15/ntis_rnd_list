from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Uid(Base):
    """data model of rnd uid table"""

    # name of table
    __tablename__ = 'uid'

    # column info
    id = Column(Integer, primary_key=True, index=True)
    serial = Column(Integer, unique=True)
    uid = Column(Integer, unique=True)

    # relationship info
    detail = relationship('Detail', back_populates='uid')


class Detail(Base):
    """data model for rnd detail table"""

    # name of table
    __table__ = 'detail'

    # column info
    id = Column(Integer, primary_key=True, index=True)
    uid_id = Column(Integer, ForeignKey('uid.id'))
    title = Column(String)
    department = Column(String)
    gov_agency = Column(String)
    date_notice = Column(DateTime)
    budget = Column(String)

    # relationship info
    uid = relationship('Uid', back_populates='detail')
    keyword = relationship('KeyWord', back_populates='detail')


class KeyWord(Base):
    """data model for KeyWords"""

    # name of table
    __table__ = 'keyword'

    # column info
    id = Column(Integer, primary_key=True, index=True)
    detail_id = Column(Integer, ForeignKey('detail.id'))
    keyword = Column(String)

    # relationship info
    detail = relationship('Detail', back_populates='keyword')


class LogScrap(Base):
    """data model for scrap log"""

    # name of table
    __table__ = 'logscrap'

    # column info
    date_scrap = Column(DateTime, primary_key=True, index=True)