import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '695aad92b9123a31eda32e1e29231ec3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_registration = {
    "name": "generate",
    "photo_id": -1
}

body_change_name = {
    "pokemon_id": "256382",
    "name": "Тест",
    "photo_id": 54
}

body_pokeball = {
    "pokemon_id": "256382"
}



'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_registration)
print(response.text)

responce_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(responce_change_name.text) '''

reponse_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(reponse_pokeball.text)

pokemon_id = reponse_pokeball.json()['id']
print(pokemon_id)