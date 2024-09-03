class Contextmanager:
    def __enter__(self):
        
        print("Risorsa acquisita")
        
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        
        if exc_type is not None:
            pass
        
        print("Risorsa rilasciata")

        return False
    
with Contextmanager() as manager:
    print("sono dentro with")