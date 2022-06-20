
class Pen:

    # atribut de clasa(static):
    brand = "Noki"

    def __init__(self, color):
        self.color = color
        self.is_empty = False

pen = Pen('red')
pen2 = Pen('black')

print(pen2.color)

print(Pen.brand)     # accesare prin clasa

print(pen.brand)     # accesare prin obiect

# toate obiectele vor impartasi acelasi atribut: brand.

Pen.brand = "no-name"

print(pen.brand)
print(pen2.brand)

