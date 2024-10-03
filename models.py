from database import db

class User(db.Model):
    __tablename__="usuarios"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    apelido =db.Column(db.String(80), unique=True)
    senha = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(15), unique=True)
    admin = db.Column(db.Boolean)

    def __init__(self, nome, email, telefone, apelido, senha, admin):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.apelido = apelido
        self.senha = senha
        self.admin = admin
    
    def __repr__(self):
        return '<User %r>' % self.apelido
        #return "Usuário: {}".format(self.nome)
    