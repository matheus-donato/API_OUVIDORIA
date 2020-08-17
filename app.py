from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from datetime import timedelta
import pandas as pd
import os

from security import authenticate, identity
from resources.user import UserRegister
from resources.classificacao import ClassificacaoOuv, ClassificacaoOuvTema
from models.tema import Tema, Subtemas

#instânciar a classe do Flask e usar a função especial __name__ que gera um nome exclusivo 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800) #token expira depois de meia hora
app.secret_key = "Inova"
api = Api(app)

temas = ['ambiente',
        'cidadania',
        'civil',
        'consumidor',
        'criminal',
        'deficiencia',
        'educacao',
        'eleitoral',
        'exec_penal',
        'familia',
        'idoso',
        'infa_infra',
        'infa_n_infra',
        'mulher',
        'outros',   
        'prisional',     
        'saude',
        'urbanistica']   

temas_certo = [
    'Ambiente',
    'Cidadania',
    'Civil',
    'Consumidor',
    'Criminal',
    'Deficiência',
    'Educação',
    'Eleitoral',
    'Execução penal',
    'Família',
    'Idoso',
    'Infância infracional',
    'Infância não infracional',
    'Mulher',
    'Outros',
    'Prisional',
    'Saúde',
    'Urbanística']




jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(ClassificacaoOuv, '/ouvidoria')
api.add_resource(ClassificacaoOuvTema, '/ouvidoria/temas')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True, port=5000)