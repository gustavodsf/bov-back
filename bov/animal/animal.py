from datetime import datetime
import enum
import uuid
from bov.web.database import db

class Sexo(enum.Enum):
  macho = 1
  femea = 2

class Raca(enum.Enum):
  zebu = 1
  europeu = 2
  mestico = 3
  industrial = 4

class Animal(db.Model):
    __tablename__ = 'animais'

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    numero_brinco = db.Column(db.Integer)
    data_nascimento = db.Column(db.DateTime)
    sexo = db.Column(db.String(100), db.Enum(Sexo))
    raca = db.Column(db.String(100), db.Enum(Raca))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'numero_brinco': self.numero_brinco,
            'data_nascimento': self.data_nascimento,
            'sexo': self.sexo,
            'raca': self.raca,
            'created_at': self.created_at.isoformat(),
        }
