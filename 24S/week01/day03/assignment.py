# a program that checks if a number added is prime
number = int(input("Enter a number to check whether it's a prime or not: "))

if number <= 1:
    print("The number cannot be prime")
else:
    i = 2
    is_prime = True
    while i * i <= number:
        if number % i == 0:
            is_prime = False
            break #exit the loop when the divisor is found
        i +=1
        
    if is_prime:
        print(f"{number} is a prime numer")
    else:
        print(f"{number} is not a prime number")
