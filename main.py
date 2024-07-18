class Voyage:
    def __init__(self, departure, destination, duration, price):
        self.departure = departure
        self.destination = destination
        self.duration = duration
        self.price = price

    def get_departure(self):
        return self.departure

    def get_destination(self):
        return self.destination

    def get_duration(self):
        return self.duration

    def get_price(self):
        return self.price

    def show_info(self):
        print(f"partenza: {self.departure}, destinazione: {self.destination}, durata: {self.duration}, prezzo: {self.price}")


class Flight(Voyage):
    def __init__(self, departure, destination, duration, price, airline_number, flight_number):
        super().__init__(departure, destination, duration, price)
        self.airline_number = airline_number
        self.flight_number = flight_number

    def get_airline_number(self):
        return self.airline_number

    def get_flight_number(self):
        return self.flight_number

    def show_info(self):
        super().show_info()
        print(f"compagnia aerea: {self.airline_number}, numero volo: {self.flight_number}")


class Train(Voyage):
    def __init__(self, departure, destination, duration, price, train_number, classs):
        super().__init__(departure, destination, duration, price)
        self.train_number = train_number
        self.classs = classs

    def get_train_number(self):
        return self.train_number

    def get_classs(self):
        return self.classs

    def show_info(self):
        super().show_info()
        print(f"numero treno: {self.train_number}, classe: {self.classs}")


class Bus(Voyage):
    def __init__(self, departure, destination, duration, price, bus_company, bus_number):
        super().__init__(departure, destination, duration, price)
        self.bus_company = bus_company
        self.bus_number = bus_number

    def get_bus_company(self):
        return self.bus_company

    def get_bus_number(self):
        return self.bus_number

    def show_info(self):
        super().show_info()
        print(f"compagnia autobus: {self.bus_company}, numero autobus: {self.bus_number}")


def main():
    f1 = Flight("Roma", "New York", 540, 850.00, "Alitalia", "AZ610")
    f2 = Flight("Milano", "Parigi", 90, 120.00, "Air France", "AF1032")

    t1 = Train("Napoli", "Roma", 70, 45.00, "FR9610", "Prima")
    t2 = Train("Firenze", "Venezia", 120, 35.00, "RV7823", "Seconda")

    b1 = Bus("Torino", "Genova", 150, 18.00, "Flixbus", "FB3201")
    b2 = Bus("Bologna", "Verona", 90, 12.00, "Itabus", "IT6754")

    flight = [f1, f2]
    for f in flight:
        f.show_info()
        print(f.get_departure())
        print(f.get_destination())
        print(f.get_duration())
        print(f.get_price())
        print(f.get_airline_number())
        print(f.get_flight_number())

    train = [t1, t2]
    for t in train:
        t.show_info()
        print(t.get_departure())
        print(t.get_destination())
        print(t.get_duration())
        print(t.get_price())
        print(t.get_train_number())
        print(t.get_classs())

    bus = [b1, b2]
    for b in bus:
        b.show_info()
        print(b.get_departure())
        print(b.get_destination())
        print(b.get_duration())
        print(b.get_price())
        print(b.get_bus_company())
        print(b.get_bus_number())


if __name__ == '__main__':
    main()
