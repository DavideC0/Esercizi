class Room:
    def __init__(self, name: str, floor: int, num_seats: int) -> None:
        self.name = name
        self.floor = floor
        self.num_seats = num_seats
        
    def set_name(self, name: str):
        self.name = name
    
    def set_floor(self, floor: int):
        self.floor = floor
        
    def set_num_seats(self, num_seats: int):
        self.num_seats = num_seats
    
    def get_name(self):
        return self.name
    
    def get_floor(self):
        return self.floor
    
    def get_num_seats(self):
        return self.num_seats