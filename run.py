from app import app
from db import db
import os

db.init_app(app)

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

@app.before_first_request
def create_tables():
    if os.path.exists('data.db') is False:    
        db.create_all()
        #add temas
        dados_subtemas = pd.read_excel('subtema.xlsx')
        for tema, tema_certo in zip(temas, temas_certo):
            Tema(tema, tema_certo).save_to_db()
        #add subtemas
        for tema, subtema in zip(dados_subtemas.tema, dados_subtemas.subtema):
            Subtemas(tema, subtema).save_to_db()