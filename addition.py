# import sys module
import sys

# assign command line arguments to variables
value1 = int(input("First number: "))
value2 = int(input("Second number: "))
value3 = int(input("Thrid number: "))

# find sum of values
result = value1 + value2 + value3

# checks if number is even or odd
if result%2 == 0:
    print ("The sum of your numbers is even")
else:
    print("The sum of your numbers is odd")
    
# print result
print("Your result is" + "result")