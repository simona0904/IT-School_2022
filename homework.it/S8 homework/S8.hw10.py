# 10) Make a function to check if the elements of a lists are equals (without using for) -> return bool


n = int(input("Enter number of elements : "))
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
print("\nList is - ", a)

def check_if_elements_of_a_list_are_equal(list):
    if a[0] == a[1]:
        return True
    else:
        return False   

print(check_if_elements_of_a_list_are_equal(a))
        