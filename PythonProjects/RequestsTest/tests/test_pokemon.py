import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e9613f2ce5c99d962b71459376b723b3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '18874'

def test_status_code(): 
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/me', headers= HEADER, params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Неджи'
