from timer import speed_deco
import requests
from flask import render_template


@speed_deco
def fetch_pokemons(index):
    '''
    This function fetches information about Pokémon from the PokeAPI based on the provided 'index'.
    It retrieves a list of Pokémon names, URLs, and their associated images.

    Args:
    index (str): The URL index for the PokeAPI endpoint to fetch Pokémon data.

    Returns:
    A rendered HTML template showing a grid of Pokémon images and navigation links.

    The function starts by making a request to the specified 'index' URL using the requests library.
    It then processes the JSON response, extracting information about individual Pokémon.
    
    For each Pokémon, it fetches additional details, such as their official artwork and an emerald version image.
    
    The function organizes this information into a list of dictionaries, where each dictionary contains:
    - 'nombre' (name of the Pokémon)
    - 'url' (URL for more details)
    - 'foto' (official artwork image URL)
    - 'foto_emerald' (emerald version image URL)
    
    The list of Pokémon data is stored in 'pokelista'. The function also constructs a 'list_nav' dictionary
    containing links for navigation to previous and next Pokémon listings.

    Finally, the function renders an HTML template named 'grid.html' and passes the 'pokelista' and 'list_nav' as data to display the Pokémon grid and navigation links.

    Example Usage:
    fetch_pokemons("https://pokeapi.co/api/v2/pokemon")

    This function can be used to fetch and display a grid of Pokémon using the PokeAPI by providing the appropriate 'index'.

    '''
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
    
    return render_template('grid.html',POKEAPI=pokelista,nav=list_nav)

