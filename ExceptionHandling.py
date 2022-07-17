# Handling exceptions using try & except block
try:
    number = input("Enter a number: ")
    number = int(number)
    print("You entered " + str(number))
except ValueError:
    print("Exception, invalid input")
else:
    print("Passed")