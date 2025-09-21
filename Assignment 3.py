#Task 1: Calculate Factorial Using a Function
def fact(n):
    if n<2:
        return 1
    else:
        return n * fact(n-1)
result=fact(5)
#print(result)

#Task 2: Using the Math Module for Calculations
import math
n=int(input("Enter the number: "))
print("Square root: ",math.sqrt(n))
print("Logarithm root: ",math.log(n))
print("Sine: ",math.sin(n))