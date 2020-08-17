from fastai.text import Learner, Path, SPProcessor, Config, SPProcessor, load_learner
import torch
import numpy as np
import sqlite3
import shutil

def _fix_sp_processor(learner: Learner, sp_path: Path, sp_model: str, sp_vocab: str) -> None:
    """
    Fixes SentencePiece paths serialized into the model.
    Parameters
    ----------
    learner
        Learner object
    sp_path
        path to the directory containing the SentencePiece model and vocabulary files.
    sp_model
        SentencePiece model filename.
    sp_vocab
        SentencePiece vocabulary filename.
    """
    for processor in learner.data.processor:
        if isinstance(processor, SPProcessor):
            processor.sp_model = sp_path / sp_model
            processor.sp_vocab = sp_path / sp_vocab

def lista_temas(tema_certo = True):
    conn = sqlite3.Connection('data.db')
    cursor = conn.cursor()
    if tema_certo:
        query = "SELECT tema_certo FROM tema"
    else:
        query = "SELECT tema FROM tema"
    cursor.execute(query)
    temas = cursor.fetchall()
    conn.close()
    return [t[0] for t in temas]

def lista_subtemas(tema):
    conn = sqlite3.Connection('data.db')
    cursor = conn.cursor()
    query = "SELECT subtema FROM subtema WHERE tema LIKE ?;"
    cursor.execute(query, (tema,))
    subtemas = cursor.fetchall()
    conn.close()
    print(subtemas)
    return [t[0] for t in subtemas]


def predict(texto:str,temas:list,model_filename:str, temas_sub:list=None):

    data_path = Config.data_path()
    name = f'ptwiki/models/tmp/'
    path_t = data_path/name
    path_t.mkdir(exist_ok=True, parents=True)

    torch.device('cpu')
            
    model_path = 'modelos'
    shutil.copy(model_path+'/spm.model', path_t)

    model = load_learner(path=model_path, file=model_filename)
    _fix_sp_processor(learner=model,sp_path=Path(model_path),sp_model="spm.model",sp_vocab="spm.vocab") 
    
    try:
        preds = np.around(np.array(model.predict(texto)[2]),3)
        preds = [float(p) for p in preds]
        if temas_sub is not None:
            return {"temas":temas, "p":preds, "temas_sub":temas_sub} 
        else:
            return {"temas":temas, "p":preds} 
    except Exception as e:
        return {"erro": str(e)}