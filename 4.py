class Ticket:
    def __init__(self, film_nomi, narx, soni):
        self.film_nomi = film_nomi
        self.narx = narx
        self.soni = soni

    def total_cost(self):
        return self.narx * self.soni

    def show_info(self):
        print(f"Film: {self.film_nomi}")
        print(f"Umumiy narx: {self.total_cost()}")


ticket = Ticket("Qasoskorlar", 40000, 3)

print(ticket.total_cost())
ticket.show_info()