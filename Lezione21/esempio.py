#first class objects
def say_hello(name:str)->None:
    print(f"Hello, {name}")

def say_ciao(name:str)->None:
    print(f"Ciao, {name}")

def saluta(func):
    func("Flavio")

print(f'First class objects')
saluta(say_hello)
saluta(say_ciao)

#inner functions
def parent():
    print(f"Sono in parent")

    def first_child():
        print(f"Sono in first child")

    def second_child():
        print(f"Sono in second child")

    second_child()
    first_child()
    return second_child

print(f'Inner functions')
out_function = parent()
print(out_function)

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

print('Decorators')
say_hello = get_time(say_hello)
say_hello("Flavio")
say_ciao = (say_ciao)
say_ciao()
random_list(10)

#context manager decorator

from contextlib import contextmanager
import time
def generatore():
    yield "A"
    yield "B"
    yield "C"    
    
print(f'Context manaher decarator')
prova_generatore = generatore()

print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))

@contextmanager
def context_manager_decorator(*args):
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time * start_time
    print(f"{elapsed_time}")
    
with context_manager_decorator() as _:
    print("ciao")
    
#thread
import time
lista_thread: list = []
def funzione(id: int):
    print(f"{id} time {time.time()}")
    time.sleep(1.5)
    print(f"{id} time {time.time()}")
    
print('Thread')
import threading
for id in range(3):
    x = threading.Thread(target=funzione, args=(id,))
    lista_thread.append(x)
    print(f"Prima di runnare il thread {time.time()}")
    x.start()
    print(f"Ho runnato il thread {time.time()}")

for t in lista_thread:
    t.join()