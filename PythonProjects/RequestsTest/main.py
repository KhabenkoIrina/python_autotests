import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e9613f2ce5c99d962b71459376b723b3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "irinahabenko9@gmail.com",
    "password": "Pokemon1203"
}
body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "235928",
    "name": "Lola",
    "photo_id": 1
}

body_id = {
    "pokemon_id": "235936"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confim_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_id)
print(response_pokeball.text)




