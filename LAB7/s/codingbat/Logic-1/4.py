def alarm_clock(day, vacation):
    weekend = (day == 0 or day == 6)
    if not vacation:
        if weekend:
            return "10:00"
        else:
            return "7:00"
    else:
        if weekend:
            return "off"
        else:
            return "10:00"
