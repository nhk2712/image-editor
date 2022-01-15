from datetime import datetime
while True:
    now=datetime.now()
    curTime=now.strftime("%H:%M:%S")
    print(curTime)