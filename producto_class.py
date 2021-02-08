class producto:
    def __init__(self, name, category, price = 0):
        self.name = name
        self.category = category
        self.price = price

    def update_price(self, percent_change, is_increased):
        if(is_increased == True):
            self.price *= ((percent_change + 100) / 100)
        elif(is_increased == False):
            self.price *= ((100 - percent_change) / 100)

    def print_info(self):
        print(f"Nombre: {self.name} \nCategoria: {self.category} \nPrecio: {int(self.price)}")