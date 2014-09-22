import pickle, urllib

banner = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
banner = pickle.loads(banner)

for line in banner:
    #print line
    #print len(line)
    print ''.join(map(lambda pair : pair[0] * pair[1], line))
