from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

import os
import boto3
from utils import _fix_sp_processor, predict, lista_temas, lista_subtemas
from models.tema import Subtemas

#Ouvidoria
class ClassificacaoOuv(Resource):
    @jwt_required()
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('texto', type=str, location='headers', required=True)
        super(ClassificacaoOuv, self).__init__()
    def post(self):
        try:
            args = self.reqparse.parse_args()
            texto = args['texto']
            modelo = 'ouvidoria-18bs-32fp.pkl'
            if not os.path.exists(f'modelos/{modelo}'):
                s3_resource = boto3.resource('s3')
                s3_resource.Object('api-ouvidoria',f'modelos/{modelo}').download_file(f'modelos/{modelo}')

            return predict(texto=texto, temas=lista_temas(), temas_sub= lista_temas(tema_certo=False), model_filename=modelo), 200
        except Exception as e:
            return {"erro": str(e)}, 500

#Subtemas
class ClassificacaoOuvTema(Resource):
    @jwt_required()
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('texto', type=str, location='headers', required=True)
        self.reqparse.add_argument('tema', type=str, location='headers',required=True)
        super(ClassificacaoOuvTema, self).__init__()

    def post(self):
        try:
            args = self.reqparse.parse_args()
            texto = args['texto']
            tema = args['tema']
            modelo = f'ouvidoria-{tema}-18bs.pkl'
            print(tema)
            if not os.path.exists(f'modelos/{modelo}'):
                s3_resource = boto3.resource('s3')
                s3_resource.Object('api-ouvidoria',f'modelos/{modelo}').download_file(f'modelos/{modelo}')
            return predict(texto=texto, temas=lista_subtemas(tema), model_filename=modelo), 200
        except Exception as e:
            return {"erro": str(e)}