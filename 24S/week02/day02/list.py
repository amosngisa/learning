[10, 20, 30, 40] #Integers
['Moses', 'Ruth', 'Richard'] #String
['Amos', 12, 40.5, ['oranges', 'mangoes']] #various data types
[] #Empty list

students = ['Richard', 'Ruth', 'Moses', 'Amos', 'Ezekiel']
numbers = [10, 11, 12]
empty = [23, 14, 6]

# print(students, numbers, empty)
# print(students[0])
# students[0] = 'Amos'
# print(students)

# List Operations
# sum = numbers * 4
# print(sum)

# Slicing
# print(students[:])
# students[3:5] = ['Jesse', 'Cyrill']
# print(students)

# List methods
# Append
t = [3, 2, 1]
t.append(4)
# extend
r = [5, 13, 10]
t.extend(r)
# sort
t.sort()

# Deleting elements
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# my_list.pop(2)
# del my_list[1]
# my_list.remove('d')
# del my_list[1:6]
# print(my_list)

# List Functions
# list = [3, 41, 12, 9, 74, 15]
# print(len(list))
# print(max(list))
# print(min(list))
# print(sum(list))
# print(sum(list)/len(list))

# challenge
total = 0
count = 0

while (True):
    prompt = input('Enter a number: ')
    if prompt == 'done':
        break
    value = int(prompt)
    total = total + value
    count = count + 1

average = total / count
print(f'Average: {average}')

# modify the code to print: sum, lenght