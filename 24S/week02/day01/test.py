# Write a program that opens a text file and iterates through 
# each line using a for loop printing each line separately

myFile = open('sample.txt')

for lineToPrint in myFile:
    lineToPrint = lineToPrint.rstrip()
    print(lineToPrint)
    