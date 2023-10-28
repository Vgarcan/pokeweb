import requests

poke_point = 'https://pokeapi.co/api/v2/pokemon/122/'

POKEAPI = requests.get(poke_point).json()




# Por cada KEY en el diccionario 
def loop_items(dict_item, lvl=0):

    INDENTATION = '--//' * lvl

    for key_item in dict_item.items():
        # imprime KEY's NAME + Tipo de contenido en ese KEY
        print(INDENTATION, key_item[0].upper(),'>>',type(key_item[1]),'<<')

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
                    loop_items(listitem, lvl= lvl+1)
                        
                        
                # Si el elemento de la lista es un LIST
                elif isinstance(listitem, list):
                    
                    # Por cada KEY en el diccionario 
                    loop_items(listitem, lvl= lvl+1)
          
        ##################################################################
            
        # Si KEY_ITEM[1] es un DICT_item                
        elif isinstance(key_item[1], dict):
            loop_items(key_item[1], lvl= lvl+1)
        
        # print(f'LVL = {lvl}')
        # lvl-=1



loop_items(POKEAPI)



