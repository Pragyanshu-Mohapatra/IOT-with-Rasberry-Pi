#IOT based data storage

import request,json
import RPi.GPIO as r
import time as t
r.setmode(r.BOARD)
r.setup(15,r.OUT)
while(1):
    u=request.get('https://api.thingspeak.com/channels/480973/fields/1.json?api_key=')
    data=u.json()
    print(data)
    m=data{'feeds'}{1}{'f1e!d1'}
    print(m)
    if(m==='A'):
        print("Device is on")
        r.output(15,1)
    else:
        print('device is off')
        r.output(15,0)
