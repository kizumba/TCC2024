import datetime
from database import db

#############################################
#USUARIO
#############################################
class Usuario(db.Model):
    __tablename__="usuarios"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    apelido =db.Column(db.String(80), unique=True)
    senha = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(15), unique=True)
    admin = db.Column(db.Boolean, default=False)

    evento_id = None

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

#############################################
#CLIENTE
#############################################
class Cliente(db.Model):
    __tablename__="clientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    telefone = db.Column(db.String(15), unique=True)
    vip = db.Column(db.Boolean, default=False)
    
    def __init__(self, nome, cpf, email, telefone, vip):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.vip = vip

    def __repr__(self):
        return "Cliente: {}".format(self.nome)

#############################################
#ARTISTA
#############################################
class Artista(db.Model):
    __tablename__="artistas"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    telefone = db.Column(db.String(15), unique=True)
    da_casa = db.Column(db.Boolean, default=False)
    
    evento_id = None

    def __init__(self, nome, cpf, email, telefone, vip):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.vip = vip

    def __repr__(self):
        return "Artista: {}".format(self.nome)

#############################################
#TIPOS ASSENTO
#############################################
class Tipo_Assento(db.Model):
    __tablename__="tipos_assentos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(256))

    assentos = db.relationship('Assento', backref='tipo_assento')
    
    def __init__(self, nome, descricao, fator_multi):
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        return "Tipo de Assento: {}".format(self.nome)

#############################################
#ASSENTO
#############################################
class Assento(db.Model):
    __tablename__="assentos"
    id = db.Column(db.Integer, primary_key=True)
    fileira = db.Column(db.String(1))
    numero = db.Column(db.Integer, unique=True)
    livre = db.Column(db.Boolean, default=True)
    
    tipo_assento_id = db.Column(db.Integer, db.ForeignKey('tipos_assentos.id'))
    tipo_assento = db.relationship('Tipo_Assento', back_populates='assentos')

    def __init__(self, nome, fileira, numero, livre):
        self.nome = nome
        self.fileira = fileira
        self.numero = numero
        self.livre = livre

    def __repr__(self):
        return "Assento da Fileira {} e Número {}".format(self.fileira, self.numero)

#############################################
#TIPOS INGRESSO
#############################################
class Tipo_Ingresso(db.Model):
    __tablename__="tipos_ingressos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True)
    fator_multi = db.Column(db.Float, default=1.0)

    ingressos = db.relationship('Ingresso', backref='tipo_ingresso')

    def __init__(self, nome, descricao, fator_multi):
        self.nome = nome
        self.descricao = descricao
        self.fator_multi = fator_multi

    def __repr__(self):
        return "Tipo de Ingressos: {}".format(self.nome)

#############################################
#INGRESSO
#############################################
class Ingresso(db.Model):
    __tablename__="ingressos"
    id = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Float)

    tipo_ingresso_id = db.Column(db.Integer, db.ForeignKey('tipos_ingressos.id'))
    tipo_ingresso = db.relationship("Tipo_Ingresso", back_populates="ingressos")

    aquisicao_id = None

    def __init__(self, preco):
        self.preco = preco

    def __repr__(self):
        return "Ingresso: R${}".format(self.preco)

#############################################
#AQUISIÇÃO
#############################################
class Aquisicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_venda = db.Column(db.DataTime, default=datetime.now())

    evento_id = None
    cliente_id = None
    
    # ingresso_id = None
    ingressos = None

    #def __init__(self):     

    def __repr__(self):
        return "Venda feita em {}".format(self.data_venda)

#############################################
#EVENTO
#############################################
class EVento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    tema = db.Column(db.String(100))
    descricao = db.Column(db.String(256))
    data = db.Column(db.Date)
    hora_inicio = db.Column(db.Time)
    duracao = db.Column(db.Float)
    lotacao = db.Column(db.Integer)

    usuario_id = None
    artista_id = None

    def __init__(self, nome, tema, descricao, data, hora_inicio, duracao, lotacao):
        self.nome = nome
        self.tema = tema
        self.descricao = descricao
        self.data = data
        self.hora_inicio = hora_inicio
        self.duracao = duracao
        self.lotacao = lotacao

    def __repr__(self):
        return "Evento: {}".format(self.nome)

# Relacionamentos exemplo
'''
https://dev.to/freddiemazzilli/flask-sqlalchemy-relationships-exploring-relationship-associations-igo

UM PARA UM

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    profile = db.relationship('Profile', uselist=False, back_populates='user')

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='profile')

UM PARA MUITOS

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    employees = db.relationship('Employee', back_populates='department')

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    department = db.relationship('Department', back_populates='employees')

MUITOS PARA MUITOS

class StudentCourses(db.Model):
    __tablename__ = 'student_courses'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    courses = db.relationship('Course', secondary=StudentCourses.__table__, back_populates='students')

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    students = db.relationship('Student', secondary=StudentCourses.__table__, back_populates='courses')

'''