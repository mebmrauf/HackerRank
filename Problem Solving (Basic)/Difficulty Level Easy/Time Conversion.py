#https://www.hackerrank.com/challenges/time-conversion

def timeConversion(s):    
    hours = int(s[:2])
    ampm = s[-2:]
    time = ''
    if ampm == 'AM' and hours == 12:
        time = '00'+s[2:-2]
    elif ampm == 'PM' and hours < 12:
        time = str(hours+12)+s[2:-2]
    else:
        time = s[0:-2]
    return time