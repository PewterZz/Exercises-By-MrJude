import os


os.chdir(r'C:\Users\ACER\Desktop')
file = open("Links.txt", "r")
file2 = open("thesecondone.txt", "w")
book = file.readlines()
count = 1
for i in book:
    print(str(count)+".", i , file=file2, end="")
    count += 1

file.close()
file2.close()
