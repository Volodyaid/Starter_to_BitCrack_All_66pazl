import subprocess
import random
import os
import random

if __name__ == "__main__":
    print ("Start")

with open('hex3.txt', 'r') as f:
    listRange = f.read().splitlines()
pos = 0
print ('All range: '+str(listRange))
while True:
        countList = listRange.__len__()
        # rndNumber = random.randrange(0, countList)
        rndSelect = str(listRange[pos])
        pos += 1
        if(pos == countList):
            pos = 0
        print ('')
        print ('Selected range: '+rndSelect)
        rangeForBC = rndSelect.split(':')

        newPos = 3
        iteration = 0
        while iteration != newPos:
            iteration += 1
            firstRange= str(rangeForBC[0])
            lastRange= str(rangeForBC[1])

            lowrange = int(firstRange, base=16) # Search range
            highrange = int(lastRange, base=16) # 1 - 
            print ('Start range: '+str(hex(lowrange)))
            print ('End range: '+str(hex(highrange)))
            highrange = highrange - 0xFFFFFFF
            res =  random.randrange(lowrange,highrange)
            diapozon = str(hex(res))
            print ('Random range: '+str(diapozon))
            cmdstr = 'cuBitCrack.exe -c -i pazl66_adress.txt -o AAAAAAA.txt  -s '+hex(res)+' -r '+'0xFFFFFFF' 
            print (cmdstr)
            subprocess.call(cmdstr)
            print ('End',diapozon)
        
