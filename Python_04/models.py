from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Usuario(db.Model):
    __tablename__ = 'ususarios'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Strng(50), unique = True, nullable = False)
    password_hash = db.Colum(db.String(255), nullable = False )
    rol = db.colum(db.String(50), default = 'Operario')
    def serializar(self)-> dict:
        return{
            "id": self.id,
            "username": self.username,
            "roll": self.rol
        }
