import requests

texto = """ 
Os médicos do hospital Ronaldo Gazzola estão roubando medicamentos na maior cara de pau. O MPRJ precisa fazer algo em relação a isso??
"""

if isinstance(texto,str):
    texto.encode("utf-8")

url = f"http://127.0.0.1:5000/classificacao/texto={texto}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))