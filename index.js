function Vehicle(make, model, year, type = 'car') {
    this.make = make;
    this.model = model;
    this.year = year;
    this.type = type;
}

const garage = [];

garage.push(new Vehicle('Honda', 'Civic', 1999));
garage.push(new Vehicle('Honda', 'Fit', 2006));
garage.push(new Vehicle('Chevrolet', 'Onix', 2020));
garage.push(new Vehicle('Chevrolet', 'Onix', 2019));
garage.push(new Vehicle('Chevrolet', 'Onix', 2018));
garage.push(new Vehicle('Fiat', 'Palio', 2015));
garage.push(new Vehicle('VolksWagen', 'Gol', 2013));
garage.push(new Vehicle('VolksWagen', 'Gol', 2008));
garage.push(new Vehicle('VolksWagen', 'Gol', 2018));
garage.push(new Vehicle('Honda', 'Civic', 2015));
garage.push(new Vehicle('Hyundai', 'HB20', 2018));
garage.push(new Vehicle('Ford', 'Ka', 2019));
garage.push(new Vehicle('Honda', 'Fit', 2019));

console.log(garage);