import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json'}
TOKEN = '26aff07461f9b121b39e96105d064216'

id = 1493

body = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_confirm = {
    "pokemon_id": "14376",
    "name": "Бульбазавр1",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_add = {
    "pokemon_id": "14376"
}

responce = requests.post(url=f'{URL}/pokemons', headers = HEADERS, json = body)

print (responce.text)

responce_confirm = requests.put(url=f'{URL}/pokemons', headers=HEADERS, json=body_confirm)

print (responce_confirm.text)

responce_add = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADERS, json=body_add)

print (responce_add.text)



