#Liv Franczykowski
#Average.py
average = 0
total = 0
howManyEntered = 0
howMany = int(input("How many test scored would you like to average?"))
testScore = int(input("Enter test score:"))
total = howManyEntered
total += testScore
howManyEntered += 1
while howManyEntered<howMany:
    testScore = int(input("Enter test score:"))
    total += testScore
    howManyEntered += 1
average = total / howMany
print("The average for the test scores you entered is:")
print(average)





    








