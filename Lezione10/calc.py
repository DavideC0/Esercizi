class Calculations:
    def __init__(self, a: float, b: float) -> None:
        self.a: float = a
        self.b: float = b
        
    def get_sum(self) -> float:
        return self.a + self.b
    
    def get_difference(self) -> float:
        return self.a - self.b
    
    def get_product(self) -> float:
        return self.a * self.b
    
    def get_quotient(self) -> float:
        return self.a / self.b