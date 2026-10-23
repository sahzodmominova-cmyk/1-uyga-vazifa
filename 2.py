class Contact:
    def __init__(self, ism, telefon):
        self.ism = ism
        self.telefon = telefon

    def update_phone(self, new_phone):
        self.telefon = new_phone

    def show_info(self):
        print(f"Ism: {self.ism}")
        print(f"Telefon: {self.telefon}")


contact = Contact("Muhammadaziz", "910432456")
contact.update_phone("931112233")
contact.show_info()