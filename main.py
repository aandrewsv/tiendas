from producto_class import producto
from tienda_class import tienda

salchichas = producto("salchichas","embutidos",1500)
durazno = producto("durazno", "fruta", 100)
oreos = producto("oreos", "snacks", 300)
pringles = producto("pringles", "snacks", 1000)

tiendalocal = tienda("tiendalocal")
tiendalocal.add_product(salchichas).add_product(durazno).add_product(oreos).add_product(pringles)

tiendalocal.set_clearance("snacks",10)


 