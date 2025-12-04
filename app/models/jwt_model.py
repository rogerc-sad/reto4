from sqlalchemy import Column, Integer, String,Boolean,DateTime, text
from sqlalchemy.orm.mapper import reconstructor
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import Boolean
from uuid import uuid4

from core.database import Base, session_db, engine
from sqlalchemy.orm.exc import NoResultFound

from datetime import datetime, timedelta
from datetime import timezone

class Jwt(Base):
    __tablename__ = "jwt"
    id = Column(String, primary_key=True, default=uuid4)
    jti = Column(String, nullable=False)
    expireAt = Column(DateTime, nullable=False)
    revoked = Column(Boolean, nullable=False)

    def __init__(self, jti,expireAt, revoked):
        self.jti = jti
        self.expireAt = expireAt
        self.revoked = revoked

    def __repr__(self):
        return {"id": self.id,"jti": self.jti,"expireAt": self.expireAt, "revoked": self.revoked}

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {"id": self.id,"jti": self.jti,"expireAt": self.expireAt, "revoked": self.revoked}

def createToken(jti: str, revoked: bool, expiresDelta: timedelta):
    expireAt = datetime.now(timezone.utc)
    if expiresDelta is None:
        expiresDelta = timedelta(seconds=10) 
    expireAt = expireAt + expiresDelta
    expireAt.replace(tzinfo=timezone.utc)

    result = []
    it1 = Jwt(jti=jti, expireAt=expireAt,revoked=revoked) 
    result =  session_db.add(it1)	
    session_db.commit()
   
    print(jti)


def revokeToken(jti: str):
    try:
        session_db.query(Jwt).filter(Jwt.jti == jti).update({Jwt.revoked: True})
        session_db.commit()
        if getToken(jti, True) is None:
            return False
        return True
    except NoResultFound as err:
        print('No existe el token')
        return False


def getToken(jti: str, revoked: bool):
    try:
        result = session_db.query(Jwt).filter(Jwt.jti==jti, Jwt.revoked==revoked).first()
        session_db.commit()    
        if result is not None:
            result = result.serialize        
        return result

    except NoResultFound as err:
        print('No existe el tokenz')
        return None 