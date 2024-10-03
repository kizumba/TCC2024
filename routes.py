from app import app
from flask import render_template
from models import User

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()

    return render_template('index.html', users=users)

@app.route('/evento')
def evento():
    return render_template('evento.html')

@app.route('/assento/<fileira>/<int:j>')
def assento(fileira,j):
    return render_template('assento.html',fileira=fileira, j=j)