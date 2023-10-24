import requests
from flask import render_template

def fetch_pokemons(index):
    POKEAPI = requests.get(index).json()

    pokelista = []
    list_nav  = []

    for item in POKEAPI['results']:
        pokemon= requests.get(item['url']).json()
        pokelista.append( 
        {
            'nombre': item['name'] , 
            'url': item['url'] ,
            'foto': pokemon['sprites']['other']['official-artwork']['front_default'], 
            'foto_emerald': pokemon['sprites']['versions']['generation-iii']['emerald']['front_default']
        }
        )
    list_nav.append( 
        { 
            'previous' : POKEAPI['previous'],
            'next' : POKEAPI['next'],
        }
        )
    print (list_nav)
    return render_template('grid.html', POKEAPI = pokelista, nav = list_nav)

