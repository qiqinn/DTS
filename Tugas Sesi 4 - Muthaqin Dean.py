timeHour = int(input("Start time in hours(0-12) : "))
timeMinute = int(input("Start time in minutes(0-59) : "))
timeDur = int(input("Event duration in minutes(0-300): "))


startTime  = str(timeHour) + "." + str(timeMinute)
print("Start time : ", startTime)


durMinutes = (timeHour * 60) + timeMinute + timeDur
durHours = durMinutes // 60
durSec = durMinutes - (durHours * 60)

print("End time :", str(durHours) + "," + str(durSec))