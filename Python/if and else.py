#BY Me
amount = int(input("enter the amount: "))
Roi = float(input("enter roi: "))
time_intv = float(input("enter time: "))

#if and else

#Class 1
if (amount > 100000):
    print("Compound interest is:", (amount * (1 + Roi/(100)) ** time_intv - amount))
else:
    print("Simple interest is:", (amount * Roi/100 * time_intv))

#Class 2

A=input("enter your word: ")
if A==A[::-1]:
    print("The word is palindrome")
else:
    print("The word is not palindrome")

# Percentage to academic class

percentage = float(input("Enter percentage of marks: "))

if percentage >= 75:
    print ("Result: First class with distinction")
elif percentage >= 60:
    print ("Result: First class")
elif percentage >= 55:
    print("Result: second class")
else:
    print("Result: third class")



#while loop

n = int(input('n: '))

x = 0

while x <= n:

    if x%3 == 0:
        print(x)

    x = x + 1

print("program exiting")



#while loop
total_students = int(input("total number of students"))

roll_no = 1
while roll_no <= total_students:

    percentage = float(input("percentage: "))

# deduce and print class corresponding to given percentage 
if percentage >= 75:
    print ("Result: First class with distinction")
elif percentage >= 60:
    print ("Result: First class")
elif percentage >= 55:
    print("Result: second class")
else:
    print("Result: third class")

roll_no = roll_no + 1