import requests


poke_point = 'https://pokeapi.co/api/v2/pokemon/122/'

def repetir_proceso(repeticion, key):
    # Si key es una LIST 
    if isinstance(key, list):
        # Nos muestra el numero de elementos en esa LIST
        print (f'-- Num. of Items = {len(key)}')

        #  Por cada ITEM en key(List)
        for listitem in key:
            # print(f'--#{i}')
            # Si el elemnto de la lista es un DICT
            if isinstance(listitem, dict):
                
                # Por cada KEY en el diccionario 
                for key_item in listitem.items():
                    # imprime KEY's NAME + Tipo de contenido en ese KEY
                    print ('--//',key_item[0],'>>',type(key),'<<')
        ##################################################################
                    
                    # Ahora analzimamos key
                    ###############################
                    repeticion(repeticion, key)
        ##################################################################

                    
        
            # Si el elemento de la lista es un LIST
            elif isinstance(listitem, list):
            # Nos muestra el numero de elementos en esa LIST
                print (f'-- Num. of Items = {len(key)}')

                #  Por cada ITEM en key(List)
                for listitem in key:
                    # print(f'--#{i}')
                    # Si el elemnto de la lista es un DICT
                    if isinstance(listitem, dict):
                        
                        # Por cada KEY en el diccionario 
                        for key_item in listitem.items():
                            # imprime KEY's NAME + Tipo de contenido en ese KEY
                            print ('--//',key_item[0],'>>',type(key),'<<')
            ##################################################################
                    
                            # Ahora analzimamos key
                            ###############################
                            repeticion(repeticion, key)
            ##################################################################

    # Si key es un DICT                
    elif isinstance(key, dict):
        for subitem in key.items():
            print ('--//',subitem[0],'>>',type(subitem[1]),'<<')

            # Ahora analzimamos key
            ###############################
            repeticion()

def obtain_pokeinfo(url,rep):
    POKEAPI = requests.get(url).json()

    # print(POKEAPI.items()['abilities'])

    # Por cada KEY en el diccionario 
    for key_item in POKEAPI.items():
        # imprime KEY's NAME + Tipo de contenido en ese KEY
        print(key_item[0].upper(),'>>',type(key_item[1]),'<<')
        
        # Ahora analzimamos key_item[1]
        ###############################
        rep(rep, key_item[1])
        
                    






obtain_pokeinfo(poke_point, repetir_proceso)



