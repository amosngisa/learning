# file = open('mbox.txt')

# count = 0

# for mistari in file:
#     count = count + 1
# print(f"Line Count: {count}")

# prompt= input("Enter the file name: ")

# try:
#     file = open(prompt)
#     for word in file:
#         if word.startswith('From'):
#             email = word.find('@')
#             after = word.find(' ', email)
#             host=word[email+1:after]
#             print(host)
# except:
#     print("File not found")

# Writing into a file
file = open('sample.txt', 'w')
text = 'Welcome Moses'
file.write(text)
file.close()
# print(file)