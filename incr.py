class Time:
  def printTime(time):
    print str(time.hours) + ":" +  \
          str(time.minutes) + ":" +  \
          str(time.seconds)
  def __init__(self,hours=10,minutes=0,seconds=0):
     self.hours=hours
     self.minutes=minutes
     self.seconds=seconds 

#currentTime=Time()
#currentTime.hours=9
#currentTime.minutes=14
#currentTime.seconds=30
currentTime=Time(10,20,30)
currentTime.printTime()

#currentTime=Time(9)
#currentTime.printTime()
