import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '695aad92b9123a31eda32e1e29231ec3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '12850'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_name_trainer():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'без опыта'
