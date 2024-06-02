class Building:
    total = 0
    name: str = None
    def __init__(self, name: str):
        Building.total += 1
        self.name = name
    def __str__(self):
        return self.name
    __repr__ = __str__


#buildings = {Building(f"Buil_{i}") for i in range(1, 41)}
buildings2 = {Building(f"Buil_{i}") for i in range(1, 41)}
#print(*buildings)
print(*buildings2, sep = "\n")
print(Building.total)


