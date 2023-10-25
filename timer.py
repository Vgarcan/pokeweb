import time

current_time= int(time.time())
print(current_time)


def speed_deco(function):
    def wrapper(*args, **kwargs):
        start_time = int(time.time())
        result = function(*args, **kwargs)## nombrado valor para devolver solo la funcion
        end_time = int(time.time())
        print(f"\n\n{function.__name__} : RUN SPEED: {end_time - start_time} seconds\n\n")
        return result##mirar esto##
    return wrapper