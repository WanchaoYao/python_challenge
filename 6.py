import zipfile

z = zipfile.ZipFile('6.zip')
number = '90052'

while True:
    fileName = number + '.txt'
    print z.getinfo(fileName).comment, 
    line = z.read(fileName)
    if line.find('Next nothing is ') != -1:
        number = line.split(' ')[-1]
    else:
        break
