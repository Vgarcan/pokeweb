import requests

poke_point = 'https://pokeapi.co/api/v2/pokemon/122/'
POKEAPI = requests.get(poke_point).json()


def loop_items(dict_item, lvl=0, mode=type):
    '''
    This function iterates through a nested dictionary and prints information about its keys and values.

    Args:
    dict_item (dict): The dictionary you want to analyze.
    lvl (int): Nesting level (default is 0).
    mode (type): A function that determines how to display the value's type (default is type).

    Usage:
    1. Provide the dictionary you want to analyze as 'dict_item'.
    2. Optionally, you can specify the initial nesting level 'lvl' (default is 0).
    3. Optionally, you can change the function for displaying the value's type using 'mode' (default is type).

    The function iterates through the dictionary, displaying keys in uppercase, the content type for each key,
    and, if a value is a list or dictionary, it shows additional information.

    Usage Example:
    example_dict = {
        'name': 'John',
        'ages': [25, 30, 35],
        'data': {
            'height': 180,
            'weight': 75
        }
    }
    loop_items(example_dict)

    This example will print information about the keys and values in 'example_dict' along with their content types.

    Note:
    If a value is a nested list or dictionary, the function will also explore those nested elements.

    '''

    INDENTATION = '--//' * lvl

    for key_item in dict_item.items():
        # Print KEY's NAME + Type of content in that KEY
        if type(key_item[1]) == dict or type(key_item[1]) == list:
            print(INDENTATION, key_item[0].upper(),'>>',type(key_item[1]),'<<')
        
        else:
            print(INDENTATION, key_item[0].upper(),'>>',mode(key_item[1]),'<<')
        
        # Now we analyze KEY_ITEM[1]
        ###############################

        # If KEY_ITEM[1] is a LIST 
        if isinstance(key_item[1], list):
            # Display the number of items in that LIST
            print (INDENTATION, f'-- Num. of Items = {len(key_item[1])}')

            # For each ITEM in KEY_ITEM[1](List)
            for listitem in key_item[1]:
                
                # If the list item is a DICT_item
                if isinstance(listitem, dict):
                    
                    # For each KEY in the dictionary 
                    loop_items(listitem, lvl= lvl+1, mode=mode)
                                     
                # If the list item is a LIST
                elif isinstance(listitem, list):
                    
                    # For each KEY in the dictionary 
                    loop_items(listitem, lvl= lvl+1, mode=mode)
          
        ##################################################################
            
        # If KEY_ITEM[1] is a DICT_item                
        elif isinstance(key_item[1], dict):

            # For each KEY in the dictionary 
            loop_items(key_item[1], lvl= lvl+1, mode=mode)



loop_items(POKEAPI, mode=str)



