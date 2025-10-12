import time
timerset = int(input('Set time in Seconds: '))

#  '//' Function ensures results are a whole number
for x in range(timerset, 0, -1):
# Hours, minutes, seconds
    hours = int(x // 3600) # 3600 seconds in a hour.
    minutes = (x % 3600) // 60 # Taking out the hour, then counting the minutes to seconds
    seconds = x % 60 # 60 seconds, standard
# Timer format
    print(f"{hours:02}'{minutes:02}'{seconds:02}")

    time.sleep(1)
print("TIME'S UP!")