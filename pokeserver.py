from flask import Flask, render_template, request
import requests
from fetching_for_grid import fetch_pokemons



########### API #############
#############################
api_offset = 0 
api_limit = 20
pokendpoint = 'pokemon' 

POKECOUNT_FOR_API = f'?offset={api_offset}&limit={api_limit}'
POKEMAIN= f'https://pokeapi.co/api/v2/{pokendpoint}{POKECOUNT_FOR_API}'
#############################



########### FLASK ###########
#############################

app= Flask(__name__)



@app.route('/')
def pokeindex ():

   return fetch_pokemons(POKEMAIN)



@app.route('/<path:url>')
def pokeindex2 (url):

    return fetch_pokemons(url)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
#############################