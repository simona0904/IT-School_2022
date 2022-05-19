producator = input("Producator: ")
model = input("Model: ")
an_fabricatie = int(input("An fabricatie: "))

if an_fabricatie >= 2000 and an_fabricatie <= 2004:
    print("Masina ta este Golf 4")
elif an_fabricatie >= 2005 and an_fabricatie <= 2010:
    print("Masina ta este Golf 5")
elif an_fabricatie >= 2011 and an_fabricatie <= 2014:
    print("Masina ta este Golf 6")    
elif an_fabricatie >= 2015 and an_fabricatie <= 2019:
    print("Masina ta este Golf 7")    
else:
    print("Masina ta este alt model") 
