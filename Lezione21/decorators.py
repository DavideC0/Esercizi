"""def get_time(func):

    def wrapper(*args):
        import time
        start = time.time()
        func(*args)
        end = time.time()
        elapsed_time = end - start
        print(f"{elapsed_time=}")

    return wrapper

def say_hello(name:str)->None:
    print(f"Hello, {name}")

@get_time
def say_ciao()->None:
    print(f"Ciao, Flavio")

@get_time
def random_list(upper_bound: int):

    import random
    import time

    sleep_time = random.randint(0, upper_bound)
    time.sleep(sleep_time)

print('Decorators')
say_hello("Flavio")
say_hello = get_time(say_hello)
say_hello("Flavio")"""

def stampa_n_volte(n:int):
    def decorator(func):
        def wrapper(*args):
            for _ in range(n):
                print(func(*args))
        return wrapper
    return decorator

@stampa_n_volte(3)
def saluta(nome):
    return f"Ciao, {nome}"

saluta("Giovanni")