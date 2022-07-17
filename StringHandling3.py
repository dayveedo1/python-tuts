name = "48" #"David Emeka"
company = "datalinks"
age = "27"
print(len(name))

print(name.find("e"))
# index -> return the index of the string parsed
# print(name.index("e"))

# isdigit -> return true or false if string has Numberic letters
print(name.isdigit())

# islower -> return true if all strings are in lowercase & false if  vice-versa
print(company.islower())

# join -> to concatenate 2 strings
str1 = "Cactus"
str2 = "Tech"
# print(join(str2))

str3 = "alphas"
print(max(str1, str2, str3))
print(min(str1, str2, str3))

# replace -> replace every occurance of 1st args with 2nd args in given string
str4 = "replacement"
print(str4.replace("e", "o"))

# upper -> converts string to upper case
print(str4.upper())

# lower -> converts string to lowercase
print(str4.lower())


