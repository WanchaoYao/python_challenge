with open('3.txt') as f:
    text = ''.join(line.rstrip() for line in f)
#print text,

result = ''
for i in range(4, len(text) - 5):
    flag = True
    string = text[i - 4 : i + 5]
    for j in range(9):
        if j == 0 or j == 4 or j == 8:
            if string[j].isupper():
                flag = False
                break
        else:
            if string[j].islower():
                flag = False
                break
    if flag:
        result += string[4]

print result
