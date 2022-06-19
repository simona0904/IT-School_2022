
# Extract the number from import_numbers variable.

import_numbers = "Today we had 280 clients."

only_numbers = [int(i) for i in import_numbers.split() if i.isdigit()]
print(only_numbers)

