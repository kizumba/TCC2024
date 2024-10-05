from app import app
from flask import render_template, request, redirect, url_for, flash
from models import *
import dados

#-------------------
#   EVENTO
#-------------------
@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    eventos = Evento.query.all()

    for evento in eventos:  
        lotacao = 0
        arrecadacao = 0
        for assento in evento.assentos:
            if not assento.livre:
                lotacao += 1
                arrecadacao += assento.preco
        evento.arrecadacao = arrecadacao
        evento.lotacao = lotacao

        db.session.commit()


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
            
            for fileira in dados.FILEIRA:
                for cadeira in range(dados.CADEIRAS):
                    assento = Assento(fileira, cadeira+1, True, 0.00, evento.id)
                    db.session.add(assento)
            
            db.session.commit()

        return redirect(url_for('index'))

@app.route('/evento/<int:id>')
def evento(id):
    evento = Evento.query.get(id)
    assentos = Assento.query.filter_by(evento_id=evento.id).all()

    if evento:
        return render_template('evento.html',evento=evento, fileira=dados.FILEIRA, cadeiras=dados.CADEIRAS, assentos=assentos)

@app.route('/evento_editar/<int:id>', methods=['GET','POST'])
def evento_editar(id):
    evento = Evento.query.get(id)
    if request.method=='GET':
        return render_template('evento_editar.html', evento=evento)
    
    if request.method=='POST':
        evento.nome = request.form.get('nome')
        evento.descricao = request.form.get('descricao')
        evento.data = request.form.get('data')
        evento.hora_inicio = request.form.get('hora')

        db.session.commit()

        return redirect(url_for('index'))


#-------------------
#   ASSENTO
#-------------------
@app.route('/assento/<fileira>/<int:numero>/<int:id>', methods=['GET','POST'])
def assento(fileira,numero,id):
    evento = Evento.query.get(id)
    assentos = Assento.query.filter_by(evento_id=id).all()
    assento = None

    for a in assentos:        
        if a.fileira == fileira and a.numero == numero:
            assento = a

    if request.method=='GET':
        print('GET',assento)
        return render_template('assento.html',fileira=fileira, numero=numero, evento=evento, assento=assento)
    
    if request.method=='POST':
        assento.preco = request.form.get('preco')
        assento.livre = False
        db.session.commit()
        # return render_template(url_for('evento',id=id))
        return redirect(url_for('assento',fileira=fileira,numero=numero,id=id))

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