# # Python Match
# # The match statement is used to perform different actions based on different conditions.
 
# day = int(input("Enter day number (1 to 7): "))

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid day number. Please enter a number between 1 and 7.")


# day = int(input("Enter day number (1 to 7): "))
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")


# # Default Value
# # Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

# day = int(input("Enter day number (6 or 7): "))
# match day:
#   case 6:
#     print("Today is Saturday")
#   case 7:
#     print("Today is Sunday")
#   case _:
#     print("Looking forward to the Weekend")


# # Combine Values
# # Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5:
#     print("Today is a weekday")
#   case 6 | 7:
#     print("I love weekends!")


# # If Statements as Guards
# # You can add if statements in the case evaluation as an extra condition-check:



# month = int(input("Enter month number (4 or 5): "))
# day = int(input("Enter day number (1 to 5): "))
# match day:
#   case 1 | 2 | 3 | 4 | 5 if month == 4:
#     print("A weekday in April")
#   case 1 | 2 | 3 | 4 | 5 if month == 5:
#     print("A weekday in May")
#   case _:
#     print("No match")


