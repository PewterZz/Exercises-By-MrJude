import os

os.chdir(r'C:\Users\ACER\Desktop')
file = open("Deok.txt", "r")
book2 = file.read()
dict = {}
list = []

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for i in book2:
    if i in punc:
        book2 = book2.replace(i, "")

book = book2.split()

for i in book:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for i in dict:
    if dict[i] == 1:
        list.append(i)

for words in list:
    print(words)
