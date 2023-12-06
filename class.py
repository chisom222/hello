class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
p = Point(2, 8)
print(p.x)
print(p.y)

d = Point(4, 6)
print(d.x)
print(d.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
        
flight = Flight(1)

people = ["Harry", "Ron", "Hermoine", "Draco"]
for person in people:
    if flight.add_passengers(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
