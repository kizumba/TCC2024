import datetime
from database import db

class Artista_Evento(db.Model):
    __tablename__='artistas_eventos'
    id = db.Column(db.Integer, primary_Key=True)
    artista_id = db.Column(db.Integer, db.ForeignKey('artistas.id'))
    evento_id = db.Column(db.Integer, db.ForeignKey('eventos.id'))

class Evento(db.Models):
    __tablename__='eventos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Strinh(100))
    descricao = db.Column(db.String(256))
    data = db.Column(db.Date)
    hora_inicio = db.Column(db.Time)

    artistas = db.relationship('Artista', secondary=Artista_Evento.__table__, back_populates='eventos')

    def __init__(self, nome, descricao, data, hora_inicio):
        self.nome = nome
        self.descricao = descricao
        self.data = data
        self.hora_inicio = hora_inicio

    def __repr__(self):
        return "Evento: {}".format(self.nome)
    

class Artista(db.Model):
    __tablename__='artistas'
    id = None
    nome = None
    cpf = None

    eventos = db.relationship('Eventos', secondary=Artista_Evento.__table__, back_populates='artistas')
    
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __repr__(self):
        return "Artista: {}".format(self.nome)

class Compra(db.Model):
    __tablename__='compras'
    id = None
    data = None

    ingresso_id = None
    evento_id = None
    cliente_id = None

    pass

class Assento(db.Model):
    __tablename__='assentos'
    id =None
    fileira = None
    numero = None

    def __init__(self, fileira, numero):
        self.fileira = fileira
        self.numero = numero

    def __repr__(self):
        return "Assento da Fileira {} e Número {}".format(self.fileira, self.numero)

class Ingresso(db.Model):
    __tablename__='ingressos'
    id = None
    preco = None

    assento_id = None

    def __init__(self, preco, nome):
        self.preco = preco
        self.nome = nome

    def __repr__(self):
        return "Ingresso para o evento {} - R${}".format(self.nome,self.preco)

class Cliente(db.model):
    __tablename__='clientes'
    id = None
    nome = None
    cpf = None
    email = None
    
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email
    
    def __repr__(self):
        return 'Cliente: {} - {}'.format(self.nome, self.email)

class Usuario(db.Model):
    __tablename__='usuarios'
    id = None
    apelido = None
    senha = None
    
    def __init__(self, apelido, senha):
        self.apelido = apelido
        self.senha = senha
    
    def __repr__(self):
        return '<User %r>' % self.apelido
        #return "Usuário: {}".format(self.nome)