#Compound Interest...
import time


Amount = float(input("enter the amount: "))
Roi = float(input("enter roi: "))
time_intv = float(input("enter time: "))

n = compounding_interest = float(input("Enter compounding period in months: "))

compound_interest_1 = Amount * (1+Roi/(100)) **time_intv - Amount

compound_interest_2 = Amount * (1+(Roi/(100 * n)))**(n * time_intv) - Amount

print("compound interest (compounded annually) after", time_intv, "years is",compound_interest_1)
print ("compound interest after", time_intv, "years is", compound_interest_2)

