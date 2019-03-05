import string

word = input("word: ").lower()

lowercase = string.ascii_lowercase #abcdefghijklmnopqrstuvwxyz

print("rot13: ", end='')
for i in range(len(word)):
    for j in range(len(lowercase)):
        if word[i] == lowercase[j]: #search for letter
            if j >= 13: print(lowercase[j-13], end='') #for the first 13 letters
            else: print(lowercase[j+13], end='') #for the last 13 letters
            break

print(" ")
