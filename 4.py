import requests

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '8022'

while True:
    r = requests.post(url + nothing)
    nothing = r.content.split()[-1]
    print r.content, nothing
