from flask import Flask, render_template
from database import db
from flask_migrate import Migrate


app = Flask(__name__)

conexao = 'sqlite:///meubanco.db'

app.config['SECRET_KEY'] = 'malmsteen o mestre'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app,db)

import routes

if __name__=='__main__':
    with app.app_context():
        db.create_all()

    app.run()