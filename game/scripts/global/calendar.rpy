init python:
    class Calendar(object):
        def __init__(self, minutes = 0, hours = 0, days = 1):
            self.minutes = minutes
            self.hours = hours
            self.days = days
        @property
        def timeString(self):
            return "Den " + str(self.days) + ", " + str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2)

        def addTime(self, minutes = 0, hours = 0, days = 0):
            self.minutes += minutes
            while self.minutes > 59:
                self.minutes -= 60
                self.hours += 1
            self.hours += hours
            while self.hours > 23:
                self.hours -= 24
                self.days += 1
            self.days += days

        def addMinutes(self, amount):
            self.addTime(amount, 0, 0)

        def addHours(self, amount):
            self.addTime(0, amount, 0)

        def addDays(self, amount):
            self.addTime(0, 0, amount)

        def isBefore(self, otherTime):
            if self.days != otherTime.days:
                return self.days < otherTime.days
            elif self.hours != otherTime.hours:
                return self.hours < otherTime.hours
            elif self.minutes != otherTime.minutes:
                return self.minutes < otherTime.minutes
            return false

        def timeOfDay(self):
            if self.hours == 7:
                return "dawn"
            elif self.hours < 18:
                return "day"
            elif self.hours == 18:
                return "dusk"
            else:
                return "night"

        def timeOfDayInt(self):
            if self.hours > 6 and self.hours < 18:
                return "day"
            else:
                return "night"
