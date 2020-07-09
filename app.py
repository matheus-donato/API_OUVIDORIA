from flask import Flask,jsonify, request
from fastai.text import Config, load_learner, Learner, Path, SPProcessor
import torch
from utils import _fix_sp_processor
import numpy as np

import os
import shutil

#instânciar a classe do Flask e usar a função especial __name__ que gera um nome exclusivo 
app = Flask(__name__)

#é preciso definir qual será o tipo de solicitação entre a API e o usuário
#usa um decorator para entender a solicitação
@app.route('/classificacao',methods = ["GET","POST"]) 
#precisamos definir um método assim que usamos um decorator
def classifica():
    
    texto = request.get_data()
    print(texto)

    data_path = Config.data_path()
    name = f'ptwiki/models/tmp/'
    path_t = data_path/name
    path_t.mkdir(exist_ok=True, parents=True)

    torch.device('cpu')
            
    model_path = 'modelos'
    shutil.copy(model_path+'/spm.model', path_t)

    model_filename = 'ouvidoria-18bs-32fp.pkl'

    model = load_learner(path=model_path, file=model_filename)
    _fix_sp_processor(learner=model,sp_path=Path(model_path),sp_model="spm.model",sp_vocab="spm.vocab")
    
    temas = ['cidadania',
             'ambiente',
             'criminal',
             'consumidor',
             'idoso',
             'saude',
             'educacao',
             'urbanistica',
             'juv_n_infra',
             'tut_juv_n_infra',
             'prisional',
             'mulher',
             'deficiencia',
             'familia',
             'juv_infra',
             'eleitoral',
             'exec_penal',
             'civil',
             'outros']    
    
    try:
        preds = np.around(np.array(model.predict(texto)[2]),3)
        preds = [float(p) for p in preds]

        resultado = {"temas":temas, "p":preds} 
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"erro":e})

if __name__ == "__main__":
    app.run(debug=True, port=5000)