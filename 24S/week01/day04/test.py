from functions import is_prime

number = int(input("Enter a number to check whether it's a prime or not: "))  
if is_prime(number):
    print(f"{number} is a prime numer")
else:
    print(f"{number} is not a prime number")