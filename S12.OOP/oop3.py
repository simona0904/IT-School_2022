from auto import Car


ford = Car(4, False, False)
vw = Car(2, True, False)
toyota = Car(4, False, True)

print("START")
print(toyota.get_gas_level())

print("Alimentam 50 litri")
toyota.refill(50)

toyota.drive(200)
print("Toyota gas:", toyota.get_gas_level())


