class Vehicle:
    def __init__(self, make, model, year, type = 'car'):
        self.make = make
        self.model = model
        self.year = year
        self.type = type

garage = []

garage.append(Vehicle('Honda', 'Civic', 1999))
garage.append(Vehicle('Honda', 'Fit', 2006))
garage.append(Vehicle('Chevrolet', 'Onix', 2020))
garage.append(Vehicle('Chevrolet', 'Onix', 2019))
garage.append(Vehicle('Chevrolet', 'Onix', 2018))
garage.append(Vehicle('Fiat', 'Palio', 2015))
garage.append(Vehicle('VolksWagen', 'Gol', 2013))
garage.append(Vehicle('VolksWagen', 'Gol', 2008))
garage.append(Vehicle('VolksWagen', 'Gol', 2018))
garage.append(Vehicle('Honda', 'Civic', 2015))
garage.append(Vehicle('Hyundai', 'HB20', 2018))
garage.append(Vehicle('Ford', 'Ka', 2019))
garage.append(Vehicle('Honda', 'Fit', 2019))

for i in range(0, len(garage)):
    print(garage[i].make, garage[i].model, garage[i].year, garage[i].type)
