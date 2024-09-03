class Pagamento:

    def __init__(self) -> None:
        self.__importo: float = 0


    def get_importo(self):
        return self.__importo

    def set_importo(self, importo: float):
        self.__importo = importo

    def dettagliPagamento(self):
        return f"Importo del pagamento: ${round(self.get_importo(), 2)}"
    
class PagamentiContanti(Pagamento):

    def __init__(self) -> None:
        super().__init__()

    def dettagliPagamento(self):
        return f"Importo del pagamento, in contanti: ${round(self.get_importo(), 2)}; in pezzi da: {self.inPezziDa()}"
    
    def inPezziDa(self):
        importo: float = self.get_importo()
        banconote: dict[int, int] = {500: 0,
                                     200: 0,
                                     100: 0,
                                     50: 0,
                                     20: 0,
                                     10: 0,
                                     5: 0
                                     }
        monete: dict[float, int] = {2.00: 0,
                                    1.00: 0,
                                    0.50: 0,
                                    0.20: 0,
                                    0.10: 0,
                                    0.05: 0,
                                    0.01: 0
                                    } 
        while importo >= 5.00:
            for key, value in banconote.items():
                if key <= importo:
                    importo = round((importo - key), 2)
                    banconote[key] += 1
                    break
        while importo < 5.00 and importo > 0.00:
            for key, value in monete.items():
                if key <= importo:
                    importo = round((importo - key), 2)
                    monete[key] += 1
                    break
        usate: dict[float, int] = {}
        for key, value in banconote.items():
            if value != 0:
                usate.update({key: value})
        for key, value in monete.items():
            if value != 0:
                usate.update({key: value})
        return usate
    
class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, nome: str, data_scadenza: str, numero: int) -> None:
        super().__init__()
        self.nome = nome
        self.data_scadenza = data_scadenza
        self.numero = numero

    def dettagliPagamento(self):
        return f"Dati della Carta di credito: {self.nome}, {self.data_scadenza}, {self.numero}; importo del pagamento: ${round(self.get_importo(), 2)}"
    

contanti1: PagamentiContanti = PagamentiContanti()
contanti2: PagamentiContanti = PagamentiContanti()
carta1: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Giovanni", "31/12/2026", 12340)
carta2: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Gigi", "31/08/2028", 98210)
contanti1.set_importo(324.99)
contanti2.set_importo(700.65)
carta1.set_importo(324.99)
carta2.set_importo(700.65)
print(contanti1.dettagliPagamento())
print(contanti2.dettagliPagamento())
print(carta1.dettagliPagamento())
print(carta2.dettagliPagamento())