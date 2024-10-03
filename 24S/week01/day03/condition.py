# if condition
x = 8
y = 12

# if x > y: #condition
#     print(x) #executed if the condition is true
# else:
#     print("X is less than y") #executes when condition is not met

# choice = input("Guess a randon letter bettwen a, b and c: ")

# if choice == 'a':
#     print("A bad guess")
# elif choice == 'b':
#     print("A good guess")
# elif choice == 'c':
#     print("Close but not correct")
    
# else:
#     print("Invalid input")

# Nested if statements
# if x == y:
#     print("X and Y are equal")
# else:
#     if x < y:
#         print("X is less than Y")
#     else:
#         print("X is greate than Y")

# catching exeptions

a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
print(a * b)
try:
    multi = int(a) * int(b)
    print(multi)
except:
    print("wrong calculation")
