# # Exception Handling
# # Error handling is the process of identifying, catching, and managing errors that occur during the execution of a program, to prevent it from crashing and to ensure smooth user experience.

# # These exceptions can be handled using the try statement:
# try:
#   print(x)
# except:
#   print("An exception occurred")

# # Error Type	Meaning
# # ZeroDivisionError - 	Jab 0 se divide karte ho

# try:
#     x = 10
#     y = 0
#     result = x / y
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Zero se divide nahi kar sakte.")

# # ValueError - 	Jab data type galat ho (string to int etc.)

# try:
#     num = int("abc")
#     print("Number:", num)
# except ValueError:
#     print("Error: Galat input diya, number expected int.")

# # TypeError - 	Jab incompatible types ko add/multiply karo

# try:
#     a = "10"
#     b = 5
#     result = a + b
#     print("Result:", result)
# except TypeError:
#     print("Error: String aur integer ko add nahi kar sakte.")

# # IndexError - 	Jab list ke bahar index access karo

# try:
#     my_list = [1, 2, 3]
#     print(my_list[5])
# except IndexError:
#     print("Error: List ke bahar ka index access karne ki koshish ki.")

# # KeyError - 	Jab dictionary mein key nahi ho

# try:
#     my_dict = {"name": "Atharva"}
#     print(my_dict["age"])
# except KeyError:
#     print("Error: Dictionary mein yeh key nahi hai.")

# # FileNotFoundError - 	Jab file exist nahi karti

# try:
#     with open("missing_file.txt", "r") as f:
#         content = f.rread()
#         print(content)
# except FileNotFoundError:
#     print("Error: File exist nahi karti.")



# # Python allows you to catch more than one exception type in a single try-except block

# try:
#     x = int(input("Enter a number: "))
#     result = 10 / x
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Error! Division by zero is not allowed.")
# except Exception as e:
#     print("Some other error occurred:", e)


# #  Catch Multiple Errors
# try:
#     num = int("abc")  
# except ValueError:
#     print("Galat input diya hai (int expected)")
# except TypeError:
#     print("Data types ka problem hai")


# # Raise an exception
# # As a Python developer you can choose to throw an exception if a condition occurs.
# # eg.1 
# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


# x = "hello"
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

