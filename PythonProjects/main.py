import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '438bedd497c8eb6f157dac82b754dc25'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Pipi",
    "photo_id": 755
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)


body_newname = {
    "pokemon_id": pokemon_id,
    "name": "NewPipi",
    "photo_id": 755
}


response_newname = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_newname)
print(response_newname.text)


body_pokeball = {
    "pokemon_id": pokemon_id
}


response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)