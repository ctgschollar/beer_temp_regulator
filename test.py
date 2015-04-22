import time
import os
on = 0
day = 0
outfile = None
os.system("gpio mode 2 out") 
while 1:
    if day != int(time.strftime("%d")):
        if not os.path.isdir("/home/pi/temp_data/%s"%time.strftime("%m")):
            os.mkdir("/home/pi/temp_data/%s"%time.strftime("%m"))
        outfile = open("/home/pi/temp_data/%s.csv"%time.strftime("%m/%d"),"a")
    
    tempfile = open("/sys/bus/w1/devices/28-000006be5c01/w1_slave")
    tempStr = tempfile.read()
    tempfile.close()
    temp = float(tempStr.split("\n")[1].split(" ")[9][2:])/1000
    print "%02.2f"%temp
    if temp > 22 and on:
        print "Turn off"
        on = 0
        os.system("gpio write 2 0")
    if temp < 20 and not on:
        print "Turn on"
        on = 1
        os.system("gpio write 2 1")
    outfile.write("%s,%d\n"%(time.strftime("%H:%M:%S"),temp))
    time.sleep(30)