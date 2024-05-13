from room import Room

class Building:
    def __init__(self, name: str, address: str, floors: int) -> None:
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms: list[Room] = []
        
    def get_rooms(self):
        return self.rooms
    
    def get_floors(self):
        return self.floors
    
    def get_name(self):
        return self.name
        
    def add_room(self, room: Room):
        if room not in self.get_rooms() and room.floor <= self.get_floors():
            self.rooms.append(room)
            return True
        return False
    
    def __str__(self) -> str:
        s = f"Building(name={self.get_name})"