import requests

poke_point = 'https://pokeapi.co/api/v2/pokemon/122/'
POKEAPI = requests.get(poke_point).json()


# Por cada KEY en el diccionario 
def loop_items(dict_item, lvl=0, mode=type):
    '''
    Esta función recorre un diccionario anidado e imprime información sobre sus claves y valores.

    Args:
    dict_item (dict): El diccionario que deseas analizar.
    lvl (int): Nivel de anidamiento (por defecto, 0).
    mode (type): Función que determina cómo mostrar el tipo de valor (por defecto, type).

    Uso:
    1. Proporciona el diccionario que deseas analizar como 'dict_item'.
    2. Opcionalmente, puedes especificar el nivel de anidamiento inicial 'lvl' (por defecto, 0).
    3. Opcionalmente, puedes cambiar la función para mostrar el tipo de valor utilizando 'mode' (por defecto, type).

    La función recorre el diccionario, mostrando las claves en mayúsculas, el tipo de contenido en cada clave
    y, si un valor es una lista o un diccionario, muestra información adicional.

    Ejemplo de uso:
    dict_ejemplo = {
        'nombre': 'Juan',
        'edades': [25, 30, 35],
        'datos': {
            'altura': 180,
            'peso': 75
        }
    }
    loop_items(dict_ejemplo)

    Este ejemplo imprimirá la información sobre las claves y valores en 'dict_ejemplo' junto con el tipo de contenido.

    Nota:
    Si el valor es una lista o un diccionario anidado, la función explorará también esos elementos anidados.

    '''

    INDENTATION = '--//' * lvl

    for key_item in dict_item.items():
        # imprime KEY's NAME + Tipo de contenido en ese KEY
        if type(key_item[1]) == dict or type(key_item[1]) == list:
            print(INDENTATION, key_item[0].upper(),'>>',type(key_item[1]),'<<')
        
        else:
            print(INDENTATION, key_item[0].upper(),'>>',mode(key_item[1]),'<<')
        
        # Ahora analzimamos KEY_ITEM[1]
        ###############################

        # Si KEY_ITEM[1] es una LIST 
        if isinstance(key_item[1], list):
            # Nos muestra el numero de elementos en esa LIST
            print (INDENTATION, f'-- Num. of Items = {len(key_item[1])}')

            #  Por cada ITEM en KEY_ITEM[1](List)
            for listitem in key_item[1]:
                
                # Si el elemnto de la lista es un DICT_item
                if isinstance(listitem, dict):
                    
                    # Por cada KEY en el diccionario 
                    loop_items(listitem, lvl= lvl+1, mode=mode)
                                     
                # Si el elemento de la lista es un LIST
                elif isinstance(listitem, list):
                    
                    # Por cada KEY en el diccionario 
                    loop_items(listitem, lvl= lvl+1, mode=mode)
          
        ##################################################################
            
        # Si KEY_ITEM[1] es un DICT_item                
        elif isinstance(key_item[1], dict):

            # Por cada KEY en el diccionario 
            loop_items(key_item[1], lvl= lvl+1, mode=mode)
        




loop_items(POKEAPI, mode=str)



