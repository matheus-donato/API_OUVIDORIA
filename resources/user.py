import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):    
    reqparser = reqparse.RequestParser()
    reqparser.add_argument('username', type=str, location="json", required=True)
    reqparser.add_argument('password', type=str, location="json", required=True)
    reqparser.add_argument('acesso', type=int, location="json", required=True)

    def post(self):
        data = UserRegister.reqparser.parse_args()

        if UserModel.find_by_username(data['username']) is not None:
            return {"message": "Um usuário com esse nome já existe"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "Usuário criado com sucesso"}, 201