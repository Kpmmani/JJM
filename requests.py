"""
import requests
x = requests.get("https://www.w3schools.com/")
print(x.text)


import random
x = open("requt.txt","x")
a = random.randrange(9000000000,9999999999)
for i in range(100+1):
    a = random.randrange(9000000000,9999999999)
    x.write(str(a)+"\n")
x.close()

"""
import requests
import re
x =requests.get("https://www.w3schools.com/")
y = x.text
a = re.findall(r'<a\s+[^>]*href="([^"]+)">([^<]+)</a>')


