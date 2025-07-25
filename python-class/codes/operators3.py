# # operators - Operators are special symbols or keywords that are used to perform operations on variables and values.


# #types of operators:
# 1. Arithmetic Operators (basic math)
# Addition +
# Subtraction	-
# Multiplication *
# Division /	
# Floor Division //	
# Modulus (remainder)	%
# Exponentiation(power) **

# num1 = 10
# num2 = 10
# answer1 = num1 + num2
# answer2= num1 - num2
# answer3 = num1 * num2
# answer4 = num1 / num2
# answer5 = num1 % num2
# print(answer1)
# print(answer2)
# print(answer3)
# print(answer4)
# print(answer5)

# adding multiple numbers:
# num1 = 10
# num2 = 35
# num3 = 45
# num4 = 12
# num5 = 40
# print(num1+num2+num3+num4+num5)

# floor divsion :  it cuts off everything after the decimal
# a =  20
# b = 3
# print(a//b)

# Exponentiation (power) : raise one number to the power of another 
# num1 = 5
# num2 = 3
# print(num1**num2)



# Assign operators: this opertors are use to assinging the value
# types of operators:

# set value =
# add and update +=
# subtract and update -=
# multiply and update *=
# modulus and update %=
# floor division and update//=
#  Exponentiation(power) **=

# a = 20
# a +=10
# print(a)




# #comparison operators :  are use to compare the two values
# Equal ==   #returns true if value are equal
# Not equal !=  #returns true if values are not equal
# Greater than > #returns true if first value is greater than second one
# Less than <    #return true is first value is smaller than first one
# Greater than or equal to >= #returns true if first value is greater or equal to other value
# Less than or equal to <=  #returns true if last value is smaller and equal to other value
 
# num1 = 10
# num2 = 10
# print(num1 <= num2)



# #Logical Operators : compare two conditions.They return True or False depending on the result of the comparison.and produce the boolean result

# and : Returns True if both statements are true  
# or : Returns True if one of the statements is true
# not :  returns False if the result is true;

# a = 15
# b = 10
# answer = (a > b) and (a == b)
# print(answer)


# x = 5
# print(not(x < 3 and x > 10))



##python  Identity Operators :
# bitwise Operators are use to perform operations on indivisual bits of numbers

# BITWISE AND &  
# rules for &
# 1 & 1 = 1
# 1 & 0 = 0
# 0 & 1 = 0
# 0 & 0 = 0


# BITWISE OR  |
# 1 | 1 = 1
# 1 | 0 = 1
# 0 | 1 = 1
# 0 | 0 = 0


# BITWISE XOR ^
# 1 ^ 1 = 0
# 1 ^ 0 = 1
# 0 ^ 1 = 1
# 0 ^ 0 = 0


# BITWISE NOT ~  
# ~1 = -2
# ~0 = -1


# BITWISE ZERO FILL LEFT SHIFT <<
# 1 << 1 = 2
# 1 << 2 = 4
# 2 << 1 = 4
# 2 << 2 = 8


# BITWISE ZERO SIGNED RIGHT SHIFT >> 
# 4 >> 1 = 2
# 4 >> 2 = 1
# 2 >> 1 = 1
# 1 >> 1 = 0



# EG for &
# a = 0b101
# b = 0b100
# c = a & b
# print(c)

# a = 5
# b = 4
# c = a >> b
# print(c)


# num1 = 6
# binary = bin(num1)
# print(binary)

# num2 = 5
# binary = bin(num2)
# print(binary)

# bitwise_and = num1 & num2
# print(bitwise_and)


