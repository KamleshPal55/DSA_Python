num1=input("Enter number1: ")
num2=input("Enter number2: ")
print(num1, num2)
#Approach 1
#num1, num2 = num2, num1
#print(num1, num2)

#Approach 2
temp = num1
num1 = num2
num2 = temp
print(num1, num2)
