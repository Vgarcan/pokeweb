import requests


poke_point = 'https://pokeapi.co/api/v2/pokemon/122/'



def obtain_pokeinfo(url):
    POKEAPI = requests.get(url).json()

    # print(POKEAPI.items()['abilities'])

    # Por cada KEY en el diccionario 
    for key_item in POKEAPI.items():
        # imprime KEY's NAME + Tipo de contenido en ese KEY
        print(key_item[0].upper(),'>>',type(key_item[1]),'<<')
        
        # Ahora analzimamos KEY_ITEM[1]
        ###############################

        # Si KEY_ITEM[1] es una LIST 
        if isinstance(key_item[1], list):
            # Nos muestra el numero de elementos en esa LIST
            print (f'-- Num. of Items = {len(key_item[1])}')

            #  Por cada ITEM en KEY_ITEM[1](List)
            for listitem in key_item[1]:
                # print(f'--#{i}')
                # Si el elemnto de la lista es un DICT
                if isinstance(listitem, dict):
                    
                    # Por cada KEY en el diccionario 
                    for key_item in listitem.items():
                        # imprime KEY's NAME + Tipo de contenido en ese KEY
                        print ('--//',key_item[0],'>>',type(key_item[1]),'<<')
            ##################################################################
                        
                        # Ahora analzimamos KEY_ITEM[1]
                        ###############################
# lvl2
                        # Si KEY_ITEM[1] es una LIST 
                        if isinstance(key_item[1], list):
                            # Nos muestra el numero de elementos en esa LIST
                            print (f'--//-- Num. of Items = {len(key_item[1])}')

                            #  Por cada ITEM en KEY_ITEM[1](List)
                            for listitem in key_item[1]:
                                # print(f'--#{i}')
                                # Si el elemnto de la lista es un DICT
                                if isinstance(listitem, dict):
                                    
                                    # Por cada KEY en el diccionario 
                                    for key_item in listitem.items():
                                        # imprime KEY's NAME + Tipo de contenido en ese KEY
                                        print ('--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                            ##################################################################
                                        # Ahora analzimamos KEY_ITEM[1]
                                        ###############################
# lvl3
                                        # Si KEY_ITEM[1] es una LIST 
                                        if isinstance(key_item[1], list):
                                            # Nos muestra el numero de elementos en esa LIST
                                            print (f'--//--//-- Num. of Items = {len(key_item[1])}')

                                            #  Por cada ITEM en KEY_ITEM[1](List)
                                            for listitem in key_item[1]:
                                                # print(f'--#{i}')
                                                # Si el elemnto de la lista es un DICT
                                                if isinstance(listitem, dict):
                                                    
                                                    # Por cada KEY en el diccionario 
                                                    for key_item in listitem.items():
                                                        # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                        print ('--//--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                                            ##################################################################
                                                    # Ahora analzimamos KEY_ITEM[1]
                                                    ###############################
# lvl4
                                                    # Si KEY_ITEM[1] es una LIST 
                                                    if isinstance(key_item[1], list):
                                                        # Nos muestra el numero de elementos en esa LIST
                                                        print (f'--//--//--//-- Num. of Items = {len(key_item[1])}')

                                                        #  Por cada ITEM en KEY_ITEM[1](List)
                                                        for listitem in key_item[1]:
                                                            # print(f'--#{i}')
                                                            # Si el elemnto de la lista es un DICT
                                                            if isinstance(listitem, dict):
                                                                
                                                                # Por cada KEY en el diccionario 
                                                                for key_item in listitem.items():
                                                                    # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                                    print ('--//--//--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                                                        ##################################################################
                                                                    # Ahora analzimamos KEY_ITEM[1]
                                                                    ###############################
# lvl5
                                                                    # Si KEY_ITEM[1] es una LIST 
                                                                    if isinstance(key_item[1], list):
                                                                        # Nos muestra el numero de elementos en esa LIST
                                                                        print (f'--//--//--//--//-- Num. of Items = {len(key_item[1])}')

                                                                        #  Por cada ITEM en KEY_ITEM[1](List)
                                                                        for listitem in key_item[1]:
                                                                            # print(f'--#{i}')
                                                                            # Si el elemnto de la lista es un DICT
                                                                            if isinstance(listitem, dict):
                                                                                
                                                                                # Por cada KEY en el diccionario 
                                                                                for key_item in listitem.items():
                                                                                    # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                                                    print ('--//--//--//--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                                                                        ##################################################################
                                                                        
                                                                        ##################################################################

                                                                                    
                                                                        
                                                                            # Si el elemento de la lista es un LIST
                                                                            elif isinstance(listitem, list):
                                                                                # Nos muestra el numero de elementos en esa LIST
                                                                                print (f'--//--//--//--//-- Num. of Items = {len(key_item[1])}')

                                                                                #  Por cada ITEM en KEY_ITEM[1](List)
                                                                                for listitem in key_item[1]:
                                                                                    # print(f'--#{i}')
                                                                                    # Si el elemnto de la lista es un DICT
                                                                                    if isinstance(listitem, dict):
                                                                                        
                                                                                        # Por cada KEY en el diccionario 
                                                                                        for key_item in listitem.items():
                                                                                            # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                                                            print ('--//--//--//--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                                                                                

                                                                    # Si KEY_ITEM[1] es un DICT                
                                                                    elif isinstance(key_item[1], dict):
                                                                        for subitem in key_item[1].items():
                                                                            print ('--//--//--//--//--//',subitem[0],'>>',type(subitem[1]),'<<')
# lvl5
                                                        ##################################################################

                                                                    
                                                        
                                                            # Si el elemento de la lista es un LIST
                                                            elif isinstance(listitem, list):
                                                                # Nos muestra el numero de elementos en esa LIST
                                                                print (f'--//--//--//-- Num. of Items = {len(key_item[1])}')

                                                                #  Por cada ITEM en KEY_ITEM[1](List)
                                                                for listitem in key_item[1]:
                                                                    # print(f'--#{i}')
                                                                    # Si el elemnto de la lista es un DICT
                                                                    if isinstance(listitem, dict):
                                                                        
                                                                        # Por cada KEY en el diccionario 
                                                                        for key_item in listitem.items():
                                                                            # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                                            print ('--//--//--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                                                

                                                    # Si KEY_ITEM[1] es un DICT                
                                                    elif isinstance(key_item[1], dict):
                                                        for subitem in key_item[1].items():
                                                            print ('--//--//--//--//',subitem[0],'>>',type(subitem[1]),'<<')
# lvl4
                                            ##################################################################

                                                        
                                            
                                                # Si el elemento de la lista es un LIST
                                                elif isinstance(listitem, list):
                                                   # Nos muestra el numero de elementos en esa LIST
                                                    print (f'--//--//-- Num. of Items = {len(key_item[1])}')

                                                    #  Por cada ITEM en KEY_ITEM[1](List)
                                                    for listitem in key_item[1]:
                                                        # print(f'--#{i}')
                                                        # Si el elemnto de la lista es un DICT
                                                        if isinstance(listitem, dict):
                                                            
                                                            # Por cada KEY en el diccionario 
                                                            for key_item in listitem.items():
                                                                # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                                print ('--//--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                        

                                        # Si KEY_ITEM[1] es un DICT                
                                        elif isinstance(key_item[1], dict):
                                            for subitem in key_item[1].items():
                                                print ('--//--//--//',subitem[0],'>>',type(subitem[1]),'<<')
# lvl3
                            ##################################################################

                                        
                            
                                # Si el elemento de la lista es un LIST
                                elif isinstance(listitem, list):
                                    # Nos muestra el numero de elementos en esa LIST
                                    print (f'--//-- Num. of Items = {len(key_item[1])}')

                                    #  Por cada ITEM en KEY_ITEM[1](List)
                                    for listitem in key_item[1]:
                                        # print(f'--#{i}')
                                        # Si el elemnto de la lista es un DICT
                                        if isinstance(listitem, dict):
                                            
                                            # Por cada KEY en el diccionario 
                                            for key_item in listitem.items():
                                                # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                print ('--//--//',key_item[0],'>>',type(key_item[1]),'<<')


                        # Si KEY_ITEM[1] es un DICT                
                        elif isinstance(key_item[1], dict):
                            for subitem in key_item[1].items():
                                print ('--//--//',subitem[0],'>>',type(subitem[1]),'<<')

                            
# lvl2
            ##################################################################

                        
            
                # Si el elemento de la lista es un LIST
                elif isinstance(listitem, list):
                   # Nos muestra el numero de elementos en esa LIST
                    print (f'-- Num. of Items = {len(key_item[1])}')

                    #  Por cada ITEM en KEY_ITEM[1](List)
                    for listitem in key_item[1]:
                        # print(f'--#{i}')
                        # Si el elemnto de la lista es un DICT
                        if isinstance(listitem, dict):
                            
                            # Por cada KEY en el diccionario 
                            for key_item in listitem.items():
                                # imprime KEY's NAME + Tipo de contenido en ese KEY
                                print ('--//',key_item[0],'>>',type(key_item[1]),'<<')


        # Si KEY_ITEM[1] es un DICT                
        elif isinstance(key_item[1], dict):
            for subitem in key_item[1].items():
                print ('--//',subitem[0],'>>',type(subitem[1]),'<<')

                # Ahora analzimamos KEY_ITEM[1]
                ###############################
# lvl2
                # Si KEY_ITEM[1] es una LIST 
                if isinstance(key_item[1], list):
                    # Nos muestra el numero de elementos en esa LIST
                    print (f'--//-- Num. of Items = {len(key_item[1])}')

                    #  Por cada ITEM en KEY_ITEM[1](List)
                    for listitem in key_item[1]:
                        # print(f'--#{i}')
                        # Si el elemnto de la lista es un DICT
                        if isinstance(listitem, dict):
                            
                            # Por cada KEY en el diccionario 
                            for key_item in listitem.items():
                                # imprime KEY's NAME + Tipo de contenido en ese KEY
                                print ('--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                    ##################################################################
                                # Ahora analzimamos KEY_ITEM[1]
                                ###############################
# lvl3
                                # Si KEY_ITEM[1] es una LIST 
                                if isinstance(key_item[1], list):
                                    # Nos muestra el numero de elementos en esa LIST
                                    print (f'--//--//-- Num. of Items = {len(key_item[1])}')

                                    #  Por cada ITEM en KEY_ITEM[1](List)
                                    for listitem in key_item[1]:
                                        # print(f'--#{i}')
                                        # Si el elemnto de la lista es un DICT
                                        if isinstance(listitem, dict):
                                            
                                            # Por cada KEY en el diccionario 
                                            for key_item in listitem.items():
                                                # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                print ('--//--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                                    ##################################################################
                                            # Ahora analzimamos KEY_ITEM[1]
                                            ###############################
# lvl4
                                            # Si KEY_ITEM[1] es una LIST 
                                            if isinstance(key_item[1], list):
                                                # Nos muestra el numero de elementos en esa LIST
                                                print (f'--//--//--//-- Num. of Items = {len(key_item[1])}')

                                                #  Por cada ITEM en KEY_ITEM[1](List)
                                                for listitem in key_item[1]:
                                                    # print(f'--#{i}')
                                                    # Si el elemnto de la lista es un DICT
                                                    if isinstance(listitem, dict):
                                                        
                                                        # Por cada KEY en el diccionario 
                                                        for key_item in listitem.items():
                                                            # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                            print ('--//--//--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                                                ##################################################################
                                                            # Ahora analzimamos KEY_ITEM[1]
                                                            ###############################
# lvl5
                                                            # Si KEY_ITEM[1] es una LIST 
                                                            if isinstance(key_item[1], list):
                                                                # Nos muestra el numero de elementos en esa LIST
                                                                print (f'--//--//--//--//-- Num. of Items = {len(key_item[1])}')

                                                                #  Por cada ITEM en KEY_ITEM[1](List)
                                                                for listitem in key_item[1]:
                                                                    # print(f'--#{i}')
                                                                    # Si el elemnto de la lista es un DICT
                                                                    if isinstance(listitem, dict):
                                                                        
                                                                        # Por cada KEY en el diccionario 
                                                                        for key_item in listitem.items():
                                                                            # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                                            print ('--//--//--//--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                                                                ##################################################################
                                                                
                                                                ##################################################################

                                                                            
                                                                
                                                                    # Si el elemento de la lista es un LIST
                                                                    elif isinstance(listitem, list):
                                                                        # Nos muestra el numero de elementos en esa LIST
                                                                        print (f'--//--//--//--//-- Num. of Items = {len(key_item[1])}')

                                                                        #  Por cada ITEM en KEY_ITEM[1](List)
                                                                        for listitem in key_item[1]:
                                                                            # print(f'--#{i}')
                                                                            # Si el elemnto de la lista es un DICT
                                                                            if isinstance(listitem, dict):
                                                                                
                                                                                # Por cada KEY en el diccionario 
                                                                                for key_item in listitem.items():
                                                                                    # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                                                    print ('--//--//--//--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                                                                        

                                                            # Si KEY_ITEM[1] es un DICT                
                                                            elif isinstance(key_item[1], dict):
                                                                for subitem in key_item[1].items():
                                                                    print ('--//--//--//--//--//',subitem[0],'>>',type(subitem[1]),'<<')
# lvl5
                                                ##################################################################

                                                            
                                                
                                                    # Si el elemento de la lista es un LIST
                                                    elif isinstance(listitem, list):
                                                        # Nos muestra el numero de elementos en esa LIST
                                                        print (f'--//--//--//-- Num. of Items = {len(key_item[1])}')

                                                        #  Por cada ITEM en KEY_ITEM[1](List)
                                                        for listitem in key_item[1]:
                                                            # print(f'--#{i}')
                                                            # Si el elemnto de la lista es un DICT
                                                            if isinstance(listitem, dict):
                                                                
                                                                # Por cada KEY en el diccionario 
                                                                for key_item in listitem.items():
                                                                    # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                                    print ('--//--//--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                                        

                                            # Si KEY_ITEM[1] es un DICT                
                                            elif isinstance(key_item[1], dict):
                                                for subitem in key_item[1].items():
                                                    print ('--//--//--//--//',subitem[0],'>>',type(subitem[1]),'<<')
# lvl4
                                    ##################################################################

                                                
                                    
                                        # Si el elemento de la lista es un LIST
                                        elif isinstance(listitem, list):
                                            # Nos muestra el numero de elementos en esa LIST
                                            print (f'--//--//-- Num. of Items = {len(key_item[1])}')

                                            #  Por cada ITEM en KEY_ITEM[1](List)
                                            for listitem in key_item[1]:
                                                # print(f'--#{i}')
                                                # Si el elemnto de la lista es un DICT
                                                if isinstance(listitem, dict):
                                                    
                                                    # Por cada KEY en el diccionario 
                                                    for key_item in listitem.items():
                                                        # imprime KEY's NAME + Tipo de contenido en ese KEY
                                                        print ('--//--//--//',key_item[0],'>>',type(key_item[1]),'<<')
                

                                # Si KEY_ITEM[1] es un DICT                
                                elif isinstance(key_item[1], dict):
                                    for subitem in key_item[1].items():
                                        print ('--//--//--//',subitem[0],'>>',type(subitem[1]),'<<')
# lvl3
                    ##################################################################

                                
                    
                        # Si el elemento de la lista es un LIST
                        elif isinstance(listitem, list):
                            # Nos muestra el numero de elementos en esa LIST
                            print (f'--//-- Num. of Items = {len(key_item[1])}')

                            #  Por cada ITEM en KEY_ITEM[1](List)
                            for listitem in key_item[1]:
                                # print(f'--#{i}')
                                # Si el elemnto de la lista es un DICT
                                if isinstance(listitem, dict):
                                    
                                    # Por cada KEY en el diccionario 
                                    for key_item in listitem.items():
                                        # imprime KEY's NAME + Tipo de contenido en ese KEY
                                        print ('--//--//',key_item[0],'>>',type(key_item[1]),'<<')


                # Si KEY_ITEM[1] es un DICT                
                elif isinstance(key_item[1], dict):
                    for subitem in key_item[1].items():
                        print ('--//--//',subitem[0],'>>',type(subitem[1]),'<<')

# lvl2






obtain_pokeinfo(poke_point)



