# API CLASSIFICAÇÃO DE TEMAS OUVIDORIA

A partir dos dados da Ouvidoria do MPRJ, foi gerado um modelo de classificação multilabel para classificar os temas e subtemas a partir dos textos das denúncias. Há também como acessar diretamente o [WebApp](https://app-ouvidoria-subtemas.herokuapp.com/) que utiliza essa API para gerar os resultados.


## Fluxo de uso

1. Crie um usuário;
2. Gere um token de usuário com suas credenciais;
3. Faça a requisição POST com o texto e receba as probabilidades de cada tema;
4. Com os temas desejados, faça as requisições POST enviando o texto e tema no qual deseja obter os subtemas.

## Temas disponíveis

* 'ambiente',
* 'cidadania',
* 'civil',
* 'consumidor',
* 'criminal',
* 'deficiencia',
* 'educacao',
* 'eleitoral',
* 'exec_penal',
* 'familia',
* 'idoso',
* 'infa_infra',
* 'infa_n_infra',
* 'mulher',
* 'outros',   
* 'prisional',     
* 'saude',
* 'urbanistica'

É necessário passar o tema <span style="color:red">**exatamente**</span> como está descrito.


## Exemplo

```
import requests
import pandas as pd
import json

```

```
########################################
#### Criando um registro de usuário ####
########################################

reg_ url = https://api-ouvidoria.herokuapp.com/register

payload = '{
    "username":<your-username>,
    "password":<your-password>,
    "acesso":2}'

headers = {'Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

```

```
################################################################
#### Gera o token para enviar a requisição de classificação ####
################################################################

token_url = "https://api-ouvidoria.herokuapp.com/auth"

payload = '{"username": "Inova","password":"inova*mprj1"}'

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

```

```
##################################
#### Classifica tema do texto ####
##################################

tema_url = "http://api-ouvidoria.herokuapp.com/ouvidoria"

headers = {
  'texto': '<texto>',
  'Authorization': 'JWT <token>'
}

response = requests.request("POST", url, headers=headers)

print(response.text.encode('utf8'))

#Resultado no formato de Dataframe

resultado_json = json.loads(resultado.text)
df = pd.DataFrame({"Promotoria": resultado_json["temas"],"Probabilidade":resultado_json["p"]})

```

```
######################################
#### Classifica subtema do texto #####
######################################

url = "http://api-ouvidoria.herokuapp.com/ouvidoria/temas"

headers = {
  'texto': '<texto>',
  'tema': '<tema>',
  'Authorization': 'JWT <token>'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

#Resultado no formato de Dataframe
resultado_json = json.loads(resultado.text)
df = pd.DataFrame({"Promotoria": resultado_json["temas"],"Probabilidade":resultado_json["p"]})
```

## Bibliotecas utilizadas na API
* Flask,
* sentencepiece,
* ninja,
* fastai
* numpy,
* Boto3,
* Flask-JWT,
* Flask-RESTful,
* FLask-SQLAlchemy,
* DateTime,
* xlrd,
* uwsgi,
* pytorch.

As versões empregadas encontram-se no arquivo [requirements.txt](https://github.com/matheus-donato/API_OUVIDORIA/blob/master/requirements.txt) para facilitação da instalação.


