import time 

seconds = 0
minutes = 0
hours = 0

timeStart = input("Start timer? y/n ")

while timeStart != "n":
    seconds += 1
    time.sleep(1)
    print(str(hours) + " Hrs " + str(minutes) + " min " + str(seconds) + " Sec ")
    if seconds == 60:
        seconds = 0
        minutes += 1
        #print(str(minutes) + " Min" )
    if minutes == 60:
        minutes = 0
        hours += 1
        #print(str(hours) + " Hrs")    
