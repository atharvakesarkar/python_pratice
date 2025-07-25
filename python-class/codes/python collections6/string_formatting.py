# # What is an f-string in Python?
# # An f-string (short for formatted string) is a way to insert variables or expressions inside a string using {}.

# name = "Atharva"
# print(f"Hello, {name}!")


# placeholder
# age = 20
# print(f"I am {age} years old.")


# # ## Expressions inside:
# a = 10
# b = 5
# print(f"Sum is {a + b}")


# ## Cleaner than + or .format()
# pi = 3.14159
# print(f"Value of pi is {pi:.3f}")


# ## Display the price with 2 decimals:
# price = 59
# txt = f"The price is {price:.3f} dollars"
# print(txt)

# # You can perform math operations on variables:
# price = 59
# tax = 0.25
# txt = f"The price is {price + (price * tax)} dollars"
# print(txt)

# # You can perform if...else statements inside the placeholders:
# price = int(input("plese enter the price: "))
# txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
# print(txt)

# Execute Functions in F-Strings
# fruit = "apples"
# txt = f"I love {fruit.upper()}"
# print(txt)

# # # Use a comma as a thousand separator:
# price = 590000000
# txt = f"The price is {price:,} dollars"
# print(txt)


# # Multiple Values
# # If you want to use more values, just add more values to the format() method:
# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))


# # ## Named Indexes
# myorder = "I have a {carname}, it is a {model}."
# print(myorder.format(carname = "Ford", model = "Mustang"))  
#  # .format() function is used to insert values into a string 


