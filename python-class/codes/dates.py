# # Python Dates
# # A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

# import datetime

# x = datetime.datetime.now()
# print(x)


# ## Return the year and name of weekday:

# import datetime
# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))


# # Creating Date Objects
# # To create a date, we can use the datetime() class (constructor) of the datetime module.
# import datetime

# x = datetime.datetime(2020, 5, 17)

# print(x)

# Display the name of the month:
# import datetime

# x = datetime.datetime(2018, 6, 1)

# print(x.strftime("%B"))