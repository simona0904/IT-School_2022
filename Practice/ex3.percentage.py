

quotient = 3 / 5
procentage = quotient * 100
print(procentage)

def percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    return str(percentage) + ' %'


print(percentage(50, 100))    