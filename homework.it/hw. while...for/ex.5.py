# 6. Intr-o cutie se află 300 de bile, numerotate cu numere începând de la unu, 
# din trei în trei. Toate bilele cărora le corespund numere pare sunt verzi. 
# Să se afle câte bile verzi sunt.



total_bile_verzi = 0

for i in range(1, 301, 3):          # trebuie pus 900 in loc de 301
    if i % 2 == 0:
        total_bile_verzi += 1
print("Total bile verzi: ", total_bile_verzi)

