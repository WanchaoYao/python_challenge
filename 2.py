text = ''
with open('2.txt') as f:
    for line in f:
        text += line
#print text,

array = [0 for i in range(128)]
for ch in text:
    array[ord(ch)] += 1
#print array

index = []
min = 1
for i in range(128):
    if array[i] == 0:
        continue
    elif array[i] < min:
        min = array[i]
        index = [i]
    elif array[i] == min:
        index.append(i)
#print index

result = ''
for ch in text:
    if ord(ch) in index:
        result += ch
        index.remove(ord(ch))
print result
