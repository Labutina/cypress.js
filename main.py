import requests
token = 'b25823bc6f10dbb748767ff448097c9d'
response = requests.post('https://pokemonbattle.me:9104/trainers/reg',
                         headers = {'content-Type' : 'application/json'},
                         json = {"trainer_token": token,
                                 "email": "germangermanqa@dolnikov.ru",
                                 "password": "Iloveqa1"})
print(response.text)



response_confirm = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email',
                                 headers = {'content-Type' : 'application/json'},
                                 json = {"trainer_token": token})
print(response_confirm.text)



add_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons',
                                     headers = {'content-Type' : 'application/json',
                                                'trainer_token' : token},
json = {"name": "Пикачу",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"})
print(add_pokemon_response.text)



response_change = requests.put('https://pokemonbattle.me:9104/pokemons',
                               headers = {'content-Type' : 'application/json',
                               'trainer_token' : token}, 
json = {
    "pokemon_id": "7877",
    "name": "Пикачу2",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})
print(response_change.text)


response_pokeball = requests.post('https://pokemonbattle.me:9104//trainers/add_pokeball',
                               headers = {'content-Type' : 'application/json',
                               'trainer_token' : token}, 
json ={"pokemon_id": "7877"})
print(response_pokeball.text)