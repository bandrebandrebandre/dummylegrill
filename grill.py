import requests
import time
import math
from datetime import datetime

url = 'http://pure-harbor-27727.herokuapp.com/temperatures'

def grill():
  while True:
    time.sleep(1)
    temp1 = int(abs(math.sin(time.time() / 90)) * 90)

    params = {'section': 1, 'temperature': temp1 + 80}
    headers= {'Content-Type': 'application/json'}

    print str(datetime.now()) + str(requests.post(url, params=params, headers=headers))
    time.sleep(1)
    temp2 = int(abs(math.sin(time.time() / 90 - 60)) * 90)

    params = {'section':2, 'temperature': temp2 + 80}
    print str(datetime.now()) + str(requests.post(url, params=params, headers=headers))

grill()
