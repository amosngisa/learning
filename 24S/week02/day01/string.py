# text = "mango is sweet" #mango is SWEET
# # print(text.upper())
# word = text[9:]
# print(word)

# count = 0
# for letter in text:
#     if letter == 'e':
#         count = count + 1
# print(count)

# check = "P" in text  #case sensitive
# print(check)

# if text == 'banana':
#     print("Yes, it is a banana")

# if text < "banana":
#     print(f"Your word, {text}, come before banana")
# elif text > "banana":
#     print(f"Your word, {text}, comes after banana")
# else:
#     print("All are bananas")

word = 'my email address is amosnyaundi4@gmail.com and is verified'

email = word.find('@')
after = word.find(' ', email)
host=word[email+1:after]
print(host)