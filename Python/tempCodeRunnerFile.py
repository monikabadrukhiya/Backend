files=open('python/check.txt','r')
date=files.readlines()
for line in date:
    word=line.split()
    print(word)