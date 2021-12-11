from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DECIMAL, DateTime

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)

    
    def __repr__(self):
        return f'Usuario {self.usuario}'

    @classmethod
    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email).one()

class Atividade(Base):
    __tablename__ = 'atividade'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    inicio = Column(DateTime(255), unique=True, nullable=False)
    fim = Column(DateTime(255), unique=True, nullable=False)
    quilometros = Column(DECIMAL(10,2), nullable=False)
    tipo = Column(String(255), nullable=False)
    local = Column(String(255), nullable=False)

    def __repr__(self):
        return f'Atividade {self.atividade}'

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    comentario = Column(String(255), nullable=True)

    def __repr__(self):
        return f'Comentario {self.comentario}'

class Curtida(Base):
    __tablename__ = 'curtida'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    def __repr__(self):
        return f'Atividade {self.curtida}'