# Operatori si operanzi aritmetici (Arithmetic Operators and Operands):

# Operators are special symbols in Python that carry out arithmetic or logical computation. 
# The value that the operator operates on is called the operand.

# ex: >>> 3+5
        # 5
# Here, + is the operator that performs addition. 2 and 3 are the operands and 5 is
# the output of the operation.        


# + , -           adunare si scadere (addition)
# *               inmultire          (multiplication)
# /               impartire          (division)
# //              impartire cu rest, dispare ce e dupa virgula
# **              ridicare la putere
# %               modulo          aflam care sunt nr pare sau impare
#                                 daca rezultatul e 0 sau 2 etc e par, daca nu impar.

# x = 15
# y = 4

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)
# print(x ** y)
# print(x % y)

# print(3 + 4 * 2)   # prima data se face inmuLtirea
# print(1 - 2)
#result =(3 + 4) * 2
# print(result)

# print(7 // 2) # catul
# print(7 % 2)  #  restul
# print(7 / 2)  # impartire cu virgula

#print(2335478 % 2)  aflam cu modulo % care sunt nr pare sau impare
#                     daca rezultatul e 0 sau 2 etc e par, daca nu impar

# print(result < 10)    False
# print(result >= 10)   True

# print(result != 10)   #diferit de 10  True


# () ** * // + -  ordinea in care se executa operatiile.



# OPERATORI LOGICI SAU BOOLIENI:

# or,and,not      logic, si logic, negatie     ex: (a or b) and c

# IDENTITY OPERATORS: 

# Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location:

# is              Returns True if both variables are the same  x = y
# is not          Returns True if a sequence with the specified value is not 
#                 present in the object.                       x is not y

#  Membership Operators:

# in              Returns True if a sequence with the specified value is present
#                 in the object                              x in y
# not in          Returns True if a sequence with the specified value is not present
#                 in the object                              x not in y
# [not]in         elementul este in colectie   ex:  1 in [1,2,3]
# is[not]         face referinta la  A = obj1; B= obj1  ex: A is B => True
#       


# Rezultatele de tip booleean sunt returnate de catre operatorii logici si de catre operatorii 
# relationali:

#   A 	      B 	 NOT A 	  A AND B 	   A OR B
#  true 	 true 	 false 	   true 	    true
#  true 	 false 	 false 	   false 	    true
#  false 	 true 	  true 	   false 	    true
#  false 	 false 	  true 	   false 	    false

# NOT este cel mai simplu operator acesta limitandu-se la inversarea valorii booleene 
# a expresiei, semnul care se utilizeaza pentru o NEGATIE LOGICA este !

# OR returneaza valoarea true daca cel putin unul dintre operanzi are valoarea 
# true, semnul care se utilizeaza pentru SAU LOgIC este ||


# AND are ca si rezultat true daca ambii operanzi au valoarea true,in restul 
# cazurilor restituind false, semnul care se utilizeaza pentru SI LOGIC este &&



# Operatorii Relationali (COMPARISON OPERATORS):

#  >       Greater than - True if left operand is greater than the right     x > y 
#  <       Less than - True if left operand is less than the right           X < Y
#  ==      Equal to - True if both operands are equal                        X == Y
#  !=      Not equal to - True if operands are not equal                     x != y
#  >=      Greater than or equal to - True if left operand is greater than or 
#          equal to the right.                                               x >= y
#  <=      Less than or equal to - True if left operand is less than or
#          equal to the right.                                               x <= y

# x = 10
# y = 12

# print(x < y)     True
# print(x > y)     False
# print(x == y)    False
# print(x != y)    True
# print(x <= y)    True
# print(x >= y)    False

# When you run a condition in an if statement, Python returns True or False:

# a = 200
# b = 33

# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")    

# Evaluate a string and a number:

# print(bool("hello"))   # True because is a str
# print(bool(15))        # True because is a int

# Evaluate two variables:

# x = "hello"
# y = 15

# print(bool(x))
# print(bool(y))

# Ex. is si is not:

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z) # True because z is the same object as x.
# print(x is y) #False because x is not the same object as y,even if they have the same content.
# print(x == y) # to demonstrate the difference betweeen "is" and "==":returns True because
#               # x is equal to y.	

# x = ["apple", "banana"]		
# y = ["apple", "banana"]	
# z = x

# print(x is not z)  False because z is the same object as x
# print(x is not y)  True because x is not the same object as y,even if they have the same content
# print(x != y)      to demonstrate the difference betweeen "is not" and "!=": this comparison 
#                     returns False because x is equal to y.

# Ex. with in, not in:

# x = ["apple", "banana"]
# # print("banana" in x)      True because a sequence with the value "banana" is in the list
# print("pineapple" not in x) True because a sequence with the value "pineapple" is not in the list
				
	

