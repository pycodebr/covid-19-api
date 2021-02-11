import requests
import json

# Link da Api #
url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

# País que deseja capturar os dados #
querystring = {"country":"Brazil"}

# Credenciais da sua conta da rapid Api #
# https://rapidapi.com/KishCom/api/covid-19-coronavirus-statistics #
headers = {
    'x-rapidapi-key': "*** SUA KEY DA API GERADA NA RAPID API ***",
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
}

# GET na Api #
response = requests.request("GET", url, headers=headers, params=querystring)

# Trata retorno da Api e mostra os dados #
dados = json.loads(response.text)
print(dados['data'])