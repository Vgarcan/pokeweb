def dict_inspect(url, lvl=0, mode=type):
    '''
    This function retrieves a JSON object from a given URL and inspects its structure, printing information about its keys and values.

    Args:
    url (str): The URL from which to fetch the JSON data.
    lvl (int): Nesting level (default is 0).
    mode (type): A function that determines how to display the value's type (default is type).

    Usage:
    1. Provide the 'url' to fetch the JSON data from.
    2. Optionally, you can specify the initial nesting level 'lvl' (default is 0).
    3. Optionally, you can change the function for displaying the value's type using 'mode' (default is type).

    The function retrieves JSON data from the specified URL, explores the structure, displays keys in uppercase, 
    the content type for each key, and, if a value is a list or dictionary, it shows additional information.

    Example Usage:
    json_url = "https://example.com/data.json"
    dict_inspect(json_url)

    This example will fetch JSON data from 'json_url' and print information about its keys and values along with their content types.

    Note:
    If a value is a nested list or dictionary, the function will also explore those nested elements.

    '''
    import requests

    dict_item = requests.get(url).json

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
                    dict_inspect(listitem, lvl= lvl+1, mode=mode)
                                     
                # If the list item is a LIST
                elif isinstance(listitem, list):
                    
                    # For each KEY in the dictionary 
                    dict_inspect(listitem, lvl= lvl+1, mode=mode)
          
        ##################################################################
            
        # If KEY_ITEM[1] is a DICT_item                
        elif isinstance(key_item[1], dict):

            # For each KEY in the dictionary 
            dict_inspect(key_item[1], lvl= lvl+1, mode=mode)
