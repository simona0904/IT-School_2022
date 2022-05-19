# 9) Make a function for printing the first 5 longest strings in a list ; (len("test"))

fruits = ["apple", "lemons", "kiwi", "oranges", "strawberries", "pears", "bananas"]

def is_the_longest_word(lst):
    def lenght_is(word):
        return len(word)

    lst.sort(key=lenght_is, reverse=True) 
    print(lst[:5])   

print(is_the_longest_word(fruits))    