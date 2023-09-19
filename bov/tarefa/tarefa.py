from datetime import datetime
import enum
import uuid
from bov.web.database import db

class Manejo(enum.Enum):
  alimentacao = 1
  sanitario = 2
  reparo = 3
  melhoria = 4

class Tarefa(db.Model):
    __tablename__ = 'tarefas'

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    titulo = db.Column(db.String(100), unique=True)
    observacao = db.Column(db.Text)
    categoria = db.Column(db.String(100), db.Enum(Manejo))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    publicado = db.Column(db.Boolean, default=False, nullable=True)

    def to_dict(self):
        return {
            'categoria': self.categoria,
            'createdAt': self.created_at.isoformat(),
            'id': self.id,
            'observacao': self.observacao,
            'publicado': self.publicado,
            'titulo': self.titulo,
            'updatedAt': self.updated_at.isoformat(),
        }
