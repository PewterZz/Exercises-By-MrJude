import os

os.chdir(r'C:\Users\ACER\Desktop')
file = open("Links.txt", "r")

text = file.read().split()
text.insert(len(text),"D")
titles = ['Mr.','Dr.','Mrs.','Jr.','Ms.']
text2 = ''
number = 0
for ele in text:
    if ele[-1] == '?' or ele[-1] == '!':
        text2 += ele+'\n'
    elif ele[-1] == '.' and ele not in titles and text[number+1][0] in 'abcdefghijklmnopqrstuvwxyz':
        text2 += ele+' '
    elif ele[-1] == '.' and ele not in titles:
        for i in text[number+1]:
            if i.isupper():
                text2 += ele+'\n'
    else:
        text2 += ele+' '
    number += 1

print(text2[:-2])

file.close()
