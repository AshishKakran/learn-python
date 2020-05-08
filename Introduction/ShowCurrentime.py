#!/usr/bin/python3

import time #import module time...see help(time)

currTime=time.time() #get current time --> UNIX epoch

totalSeconds=int(currTime)

currSecond = totalSeconds % 60
totalMinutes= totalSeconds // 60
currMinute= totalMinutes % 60
totalHours = totalMinutes // 60
currHour = totalHours % 24

print("Current time is ",currHour,":",currMinute,":",currSecond, "GMT") 
