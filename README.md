# API CLASSIFICAÇÃO DE TEMAS OUVIDORIA

A partir dos dados da Ouvidoria do MPRJ, foi gerado um modelo de classificação multilabel para classificar os temas das denúncias. É utilizado o pacote Fast.ai para a criação do modelo, que foi exportado e será consumido por essa API.

# Exemplo

> Python

```
import requests
import pandas as pd
import json

texto = """ 
Os médicos do hospital Ronaldo Gazzola estão roubando medicamentos na maior cara de pau. O MPRJ precisa fazer algo em relação a isso!!
"""

texto = "Os hospitais da Caxias estão super lotados, os remedios sumiram junto com os médicos. O MP precisa fazer algo!!"

url = "https://api-ouvidoria.herokuapp.com/classificacao"

payload = [{'texto': f"{texto}"}]
headers = {
    'Content-Type': 'application/json'
    }

resultado = requests.request("POST", url, headers=headers, data = str(payload))

resultado_json = json.loads(resultado.text)
df = pd.DataFrame({"Promotoria": resultado_json["temas"],"Probabilidade":resultado_json["p"]})
```


