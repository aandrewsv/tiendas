from producto_class import producto

class tienda:
    def __init__(self, name):
        self.name = name
        self.productlist = [] 
    
    def add_product(self, new_product):
        self.productlist.append(new_product)
        return self
    def sell_product(self, id):
        self.productlist[id].print_info()
        self.productlist.pop(id)
        return self
    def inflation(self, percent_increase):
        for i in self.productlist:
            i.update_price(percent_increase, True)
        return self
    def set_clearance(self, category, percent_discount):
        for i in self.productlist:
            if i.category == category:
                i.update_price(percent_discount, False)
                i.print_info()
        return self