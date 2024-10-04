from app import app
from flask import render_template
#from models import *
from dados import *

# eventos = [evento1, evento2, evento3]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',eventos=eventos)

@app.route('/evento/<int:id>')
def evento(id):
    
    return render_template('evento.html',id=id)

@app.route('/assento/<fileira>/<int:j>/<int:id>')
def assento(fileira,j,id):
    return render_template('assento.html',fileira=fileira, j=j,id=id)

@app.route('/venda')
def ingresso():
    return render_template('venda.html')