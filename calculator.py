def to_minutes(hour, minute, ampm):

    #set the hour input in integer
    hour = int(hour)
    #set the minute input in integer
    minute = int(minute)

    #If time is on PM and its hour is not 12, convert it into 24-hour format
    if ampm == "PM" and hour != 12:
        hour += 12
    #If time is on AM and its hour is 12, adjust the hour to 0
    if ampm == "AM" and hour == 12:
        hour = 0

    #turn the total time into minutes and return it
    return hour * 60 + minute 