from app import app
from flask import render_template, request, redirect, url_for, flash
from models import *

#-------------------
#   EVENTO
#-------------------
@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    eventos = Evento.query.all()

    if request.method=='GET':
        return render_template('index.html', eventos=eventos)
    
    if request.method=='POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        data = request.form.get('data')
        hora = request.form.get('hora')
        usuario_id = 1
        
        evento = Evento(nome, descricao, data, hora, usuario_id)
        if evento:
            db.session.add(evento)
            db.session.commit()

        return redirect(url_for('index'))

@app.route('/evento/<int:id>')
def evento(id):
    evento = Evento.query.get(id)
    if evento:
        return render_template('evento.html',evento=evento)

#-------------------
#   ASSENTO
#-------------------
@app.route('/assento/<fileira>/<int:numero>/<int:id>')
def assento(fileira,numero,id):
    evento = Evento.query.get(id)
    livre = False
    return render_template('assento.html',fileira=fileira, numero=numero, evento=evento, livre=livre)

#-------------------
#   CLIENTE
#-------------------
@app.route('/cliente_lista', methods=['GET', 'POST'])
def cliente_lista():
    clientes = Cliente.query.all()
    if request.method == 'GET':
        return render_template('cliente_lista.html', clientes=clientes)
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        email = request.form.get('email')
        
        cliente = Cliente(nome, cpf, email)
        if evento:
            db.session.add(cliente)
            db.session.commit()
        return redirect(url_for('cliente_lista'))


@app.route('/cliente_ver/<int:id>')
def cliente_ver(id):
    cliente = Cliente.query.get(id)
    clientes_eventos = Cliente_Evento.query.all()
    lista_eventos = []
    for cliente_evento in clientes_eventos:
        if cliente_evento.evento_id == cliente.id:
            evento = Evento.query.get(cliente_evento.cliente_id) 
            print('Evento add: ', evento)
            lista_eventos.append(evento)
    return render_template('cliente_ver.html',cliente=cliente, lista_eventos=lista_eventos)

@app.route('/progresso')
def progresso():
    return render_template('progresso.html')