from app import app
from flask import render_template
from models import *

@app.route('/')
@app.route('/index')
def index():
    usuarios = Usuario.query.all()

    return render_template('index.html', usuarios=usuarios)
    #return render_template('index.html')

@app.route('/evento')
def evento():
    return render_template('evento.html')

@app.route('/assento/<fileira>/<int:j>')
def assento(fileira,j):
    return render_template('assento.html',fileira=fileira, j=j)