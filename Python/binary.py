A=input("enter your word: ")
if A==A[::-1]:
    print("The word is palindrome")
else:
    print("The word is not palindrome")


n = int(input("Enter a number:"))

if n%2 == 0:
    print("even")

else:
    print("odd")

tenth_percentage = int(input("Enter 10th Percent:"))
twelfth_percentage = int(input("Enter 12th percent:"))

if (tenth_percentage > 80) or (twelfth_percentage > 70) :
    print("student is eligible for scholarship")
else:
    print("student is not eligible for scholarship")