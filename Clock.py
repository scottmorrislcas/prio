import time
from datetime import datetime
while True:
    now = datetime.now()  
    print ("%s:%s" % (now.hour,now.minute)) 
    told = ("%s:%s" % (now.hour,now.minute))
    time.sleep(1)
    if told == told:
        break
