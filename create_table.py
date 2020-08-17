import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()


# PRECISA SER INTEGER
# Esse é o único lugar onde int vs INTEGER fazer diferença de ser colocado para as colunas serem auto-incrementais
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text, acesso int)"
cursor.execute(create_table)

# Tabela de temas
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

temas_certo = [
    'Cidadania',
    'Ambiente',
    'Criminal',
    'Consumidor',
    'Idoso',
    'Saúde',
    'Educação',
    'Urbanística',
    'Juventude não infracional',
    'Tutela juventude não infracional',
    'Prisional',
    'Mulher',
    'Deficiência',
    'Família',
    'Juventude infracional',
    'Eleitoral',
    'Execução penal',
    'Civil',
    'Outros'
]

create_table = "CREATE TABLE IF NOT EXISTS tema (tema_id INTEGER PRIMARY KEY,tema text, tema_certo texto)"
cursor.execute(create_table)

query = "INSERT INTO tema VALUES (NULL, ?, ?)"
cursor.executemany(query, zip(temas, temas_certo))

connection.commit()

connection.close()