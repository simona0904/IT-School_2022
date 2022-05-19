# 10) Make a function to check if the elements of a lists are equals (without using for) -> return bool




def check_if_elements_of_a_list_are_equal(numbers):
    if numbers.count(numbers[0]) == len(numbers):
        return True
    else:
        return False  


print(check_if_elements_of_a_list_are_equal([5, 2]))
print(check_if_elements_of_a_list_are_equal([2, 2, 5]))
print(check_if_elements_of_a_list_are_equal([2, 2]))
