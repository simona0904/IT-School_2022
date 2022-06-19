
# 2) Replace with "x" last char in each product_code_list element.

product_code_list = [
    "mmf2",
    "xdfr",
    "ef3r",
    "efc2",
    "sddf",
    "weee"
]

replaced_product_code_list = []

for product in product_code_list:
    replaced_product = product[0:-1] + "x"
    replaced_product_code_list.append(replaced_product)
    print(replaced_product)

  
 
