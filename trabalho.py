import requests as rq

print("Usando Req Res API, Listando todos os Usuários: GET")
api_url = 'https://reqres.in/api/users?page=2'
response = rq.get(api_url)
print(response.json())

##
print("Usando Req Res API, Listando o usuário de ID 2: GET")
api_url = 'https://reqres.in/api/users/2'

response = rq.get(api_url)
print(response.json())

##
print("Usando Req Res API, Criando Usuário: POST")
api_url = 'https://reqres.in/api/users'
data = {
    "name": "morpheus",
    "job": "leader"
}

response = rq.post(api_url, data=data)
print(response.json())

##
print("Usando Fake Rest API, Pegando todas as Atividades: GET")
api_url = 'https://fakerestapi.azurewebsites.net/api/Activities'
response = rq.get(api_url)
print(response.json())

##
print("Usando Fake Rest API, Criando Atividade: POST")
api_url = 'https://fakerestapi.azurewebsites.net/api/Activities'
response = rq.post(api_url, data="CORPO", headers={'Content-Type':'application/json'})
print(response.json())
print("Status: " + str(response.status_code))

##

