import os


os.chdir(r'C:\Users\ACER\Desktop')
file = open("Deok.txt", "r")
book = file.readlines()
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

count = -1
for i in book:
    count += 1
    for b in i:
        if b in punc:
            book.pop(count)
            damn = i.replace(b, "")
            book.insert(count,damn)


words = 0
for i in book:
    word = i.split()
    for werd in word:
        words += 1

letters = 0
for i in book:
    letter = i.split()
    for wook in letter:
        for bro in wook:
            letters += 1

print(f"Average word count of this book is {letters/words}")

file.close()
