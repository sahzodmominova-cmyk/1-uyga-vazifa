class Athlete:
    def __init__(self, ism, sport_turi, yosh):
        self.ism = ism
        self.sport_turi = sport_turi
        self.yosh = yosh

    def show_info(self):
        print(f"Ism: {self.ism}")
        print(f"Sport turi: {self.sport_turi}")
        print(f"Yosh: {self.yosh}")


athlete = Athlete("Ali", "Futbol", 20)
athlete.show_info()