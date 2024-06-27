#first class objects
"""def say_hello(name:str)->None:
    print(f"Hello, {name}")

def say_ciao(name:str)->None:
    print(f"Ciao, {name}")

def saluta(func):
    func("Flavio")

saluta(say_hello)
saluta(say_ciao)"""

#inner functions
"""def parent():
    print(f"Sono in parent")

    def first_child():
        print(f"Sono in first child")

    def second_child():
        print(f"Sono in second child")

    second_child()
    first_child()
    return second_child

out_function = parent()
print(out_function)"""

#Decorators

def get_time(func):

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

say_hello = get_time(say_hello)
say_hello("Flavio")
say_ciao = (say_ciao)
say_ciao()
random_list()