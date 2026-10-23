class Player:
    def __init__(self, ism):
        self.ism = ism
        self.energiya = 100

    def use_energy(self, amount):
        self.energiya = max(0, self.energiya - amount)

    def show_status(self):
        print(f"Oyinchi: {self.ism}")
        print(f"Energiya: {self.energiya}")


player = Player("artishok")
player.use_energy(35)
player.show_status()