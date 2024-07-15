class Sporty:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_nationality(self):
        return self.nationality

    def show_info(self):
        print(f"nome: {self.name}, age: {self.age}, nazionalita': {self.nationality}")


class SoccerPlayer(Sporty):
    def __init__(self, name, age, nationality, team, position):
        super().__init__(name, age, nationality)
        self.team = team
        self.position = position

    def get_team(self):
        return self.team

    def get_position(self):
        return self.position

    def show_info(self):
        super().show_info()
        print(f"squadra: {self.team}, posizione: {self.position}")


class TennisPlayer(Sporty):
    def __init__(self, name, age, nationality, atp_wta_rankings):
        super().__init__(name, age, nationality)
        self.atp_wta_rankings = atp_wta_rankings

    def get_atp_wta_rankings(self):
        return self.atp_wta_rankings

    def show_info(self):
        super().show_info()
        print(f"atp_wta_rankings: {self.atp_wta_rankings}")


def main():
    s = SoccerPlayer("Cristiano Ronaldo", 36, "Portoghese", "Manchester United", "Attaccante")
    t = TennisPlayer("Roger Federer", 40, "Svizzero", 8)

    s.show_info()
    print()
    t.show_info()
    print()

    print(s.get_name())
    print(s.get_age())
    print(s.get_position())
    print(s.get_nationality())
    print(s.get_team())

    print(t.get_name())
    print(t.get_age())
    print(t.get_nationality())
    print(t.get_atp_wta_rankings())


if __name__ == '__main__':
    main()
