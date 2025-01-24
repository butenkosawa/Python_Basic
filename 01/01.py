# import math
# import sys
import requests
from math import pi

print ('Hello, world!')
# print (sys.argv[0])
# print (sys.argv[1])
print(pi)

response = requests.get('https://flowers.ua/')
print(response.status_code)
print(response.text)