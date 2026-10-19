# Natural number > 1, which has only 2 factors 1 and itself
# 19 => 1 and 19 == Prime number
# 28 => 1, 2, 4, 7, 14, 28 == not a prime number

num = int(input("Enter a number: "))
count = 0
if num > 1:
    for i in range(1, num+1):
        if num%i == 0:
            count = count + 1
    if count == 2:
        print("The number is prime")
    else:
        print("The number is not prime")