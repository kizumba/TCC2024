from database import db

#---------------------------
#   CLIENTE E EVENTOS
#---------------------------
class Cliente_Evento(db.Model):
    __tablename__ = 'clientes_eventos'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('eventos.id'))
    evento_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))

#---------------------------
#   EVENTOS
#---------------------------
class Evento(db.Model):
    __tablename__ = 'eventos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(256))
    data = db.Column(db.String(10))
    hora_inicio = db.Column(db.String(5))
    
    #um evento muito assentos
    assentos = db.relationship('Assento', back_populates='evento')

    #muito eventos um usuário
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    usuario = db.relationship('Usuario', back_populates='eventos')

    #muitos eventos muitos clientes
    clientes = db.relationship('Cliente', 
                               secondary=Cliente_Evento.__table__, 
                               back_populates='eventos')

    def __init__(self, nome, descricao, data, hora_inicio, usuario_id):
        self.nome = nome
        self.descricao = descricao
        self.data = data
        self.hora_inicio = hora_inicio
        self.usuario_id = usuario_id

    def __repr__(self):
        return "Evento: {}".format(self.nome)

#---------------------------
#   CLIENTES
#---------------------------
class Cliente(db.Model):
    __tablename__='clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(100))
    
    #muitos clientes muitos eventos
    eventos = db.relationship('Evento', 
                              secondary=Cliente_Evento.__table__, 
                              back_populates='clientes'
                              )

    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email
    
    def __repr__(self):
        return 'Cliente: {} - {}'.format(self.nome, self.email)
    


#---------------------------
#   ASSENTOS
#---------------------------
class Assento(db.Model):
    __tablename__='assentos'
    id = db.Column(db.Integer, primary_key=True)
    fileira = db.Column(db.String(1))
    numero = db.Column(db.Integer)
    livre = db.Column(db.Boolean)
    preco = db.Column(db.Float)

    #um assento muito eventos
    evento_id = db.Column(db.Integer, db.ForeignKey('eventos.id'))
    evento = db.relationship('Evento', back_populates='assentos')

    def __init__(self, fileira, numero, livre, preco, evento_id):
        self.fileira = fileira
        self.numero = numero
        self.livre = livre
        self.preco = preco
        self.evento_id = evento_id

    def __repr__(self):
        return "Fileira: {}, Número: {}, Ocupado: {}.".format(self.fileira, self.numero, self.livre)
        # return "{}, {}, {}, {}, {}\n".format(self.fileira, self.numero, self.livre, self.preco, self.evento_id)

#---------------------------
#   USUÁRIOS
#---------------------------
class Usuario(db.Model):
    __tablename__='usuarios'
    id = db.Column(db.Integer, primary_key=True)
    apelido = db.Column(db.String(100), unique=True)
    senha = db.Column(db.String(100))
    
    #um usuário muitos eventos
    eventos = db.relationship('Evento', back_populates='usuario')

    def __init__(self, apelido, senha):
        self.apelido = apelido
        self.senha = senha
    
    def __repr__(self):
        return "Usuário: {}".format(self.apelido)