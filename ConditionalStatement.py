# *** WORKING WITH CONDITIONAL STATEMENTS ***
# IF STATEMENT
# ELIF STATEMENT (ELIF)
# OR OPERATOR
# AND OPERATOR
# NOT OPERATOR

# IF-ELSE Condition
raining = False
if raining:
    print("Take an umbrella")
else:
    print("Leave umbrella at home")

# Conditional expression
coldWeather = False
sunny = False
humid = True

# OR OPERATOR
if coldWeather == True or humid == True:
    print("Go and swim")
elif sunny == True: # sunny
    print("Take sunglasses")
else:
    print("Lie down at home & sleep")


age = 27
sex = "male"

# AND OPERATOR
if age == 27 and sex == "male":
    print("Pass")
else:
    print("Fail")

firstName = "Emeka"
lastName = "Amadi"

# NOT OPERATOR
if not firstName == "Emeka" and lastName == "Amadi":
    print("InCorrect")
else:
    print("Correct")


# GRADING SHEET

try:
    score = input("Enter a score: ")
    score = float(score)  # convert score from string to int


    if score >= 70 and score <= 100:
        grade = "A"
        print("Grade is %s " % grade)
    elif 60 <= score <= 69:
        grade = "B"
        print("Grade is %s " % grade)
    elif 50 <= score <= 59:
        grade = "C"
        print("Grade is %s " % grade)
    elif 50 > score >= 0:
        grade = "D"
        print("Grade is %s " % grade)
    else:
        print("Invalid Score")
except ValueError:
    print("Exception encountered")


