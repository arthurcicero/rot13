import string

word = input("word: ").lower()

lowercase = string.ascii_lowercase

print("rot13: ", end='')
for i in range(len(word)):
    for j in range(len(lowercase)):
        if word[i] == lowercase[j]:
            if j >= 13: print(lowercase[j-13], end='') #first 13 letters
            else: print(lowercase[j+13], end='') #last 13 letters
            break

print(" ")
