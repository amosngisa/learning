# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f'{i * j:3}', end=' ')
#     print()

word = "PYTHON"

# Outer loop for each line
for i in range(len(word)):
    # Print the rotated word with spaces between the letters
    for j in range(len(word)):
        print(f"{word[(i + j) % len(word)]} ", end="")
    print()  # Move to the next line after each row
