line = input("Enter a word:")
line = line.lower()
print(line)

count = 0
count_2 = 0
for vowel in line:
    if vowel == 'a':
        count = count + 1
    elif vowel == 'e':
        count = count + 1
    elif vowel == 'i':
        count = count + 1
    elif vowel == 'o':
        count = count + 1
    elif vowel == 'u':
        count = count + 1
    elif vowel == 'y':
        count = count + 1
    else:
        count_2 = count_2 + 1

count = str(count)
count_2 = str(count_2)
print("Vowels = " + count)
print("Consonants = " + count_2) 

