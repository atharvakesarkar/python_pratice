# #loop is used to repeat some code again and again.
# #We use it when we want to do the same thing multiple times without writing it again and again.

# #type of loop:
# # 1.while loop
# # 2. for loop


# # While loop:
# # A while loop keeps running as long as a condition is true.As soon as the condition becomes false, the loop stops.
# i = 0
# while i < 101:
#     print(i)
#     i += 1


# # The break Statement
# # With the break statement we can stop the loop even if the while condition is true:

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# # The continue Statement
# # With the continue statement we can stop the current iteration, and continue with the next:

# i = 0
# while i < 6:
#   i += 1
#   if i == 7:
#     continue
#   print(i)


# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
