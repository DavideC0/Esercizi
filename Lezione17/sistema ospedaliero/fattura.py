from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self, lista_pazienti: list[Paziente], dottore: Dottore) -> None:
        if dottore.isValid():
            self.lista_pazienti: list = lista_pazienti
            self.dottore: Dottore = dottore
            self.fatture: int = len(self.lista_pazienti)