# def sum(a,b):
#     print(a+b)
    
# sum(2,5)

# def hello():
#     print('Hello World')
    
# hello()

def is_prime(number):
    if number <= 1:
       return False
    else:
        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
            i +=1
        return True
    

# number = int(input("Enter a number to check whether it's a prime or not: "))  
# if is_prime(number):
#     print(f"{number} is a prime numer")
# else:
#     print(f"{number} is not a prime number")

# text = [23, 11]
# print(len(text))

# import math

# print(math.sqrt(2))

import random

# guess = [1,2,3]
# x = random.choice(guess)
# print(x)

# def lyrics():
#     print("I sleep all night and work all day")
    

# lyrics()

choices = random.choice(['Rock', 'Paper', 'Sciciors'])

print(choices)
