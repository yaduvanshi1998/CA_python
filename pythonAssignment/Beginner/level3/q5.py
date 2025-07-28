"""5. Create a class 'Time' and initialize it with hours and minutes.
    Create a method addTime() which should take two Time objects and add them.
    E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
    Create another method displayTime() which should print the time.
    Also, create a method displayMinute() which should display the total minutes in the Time.
    E.g.- (1 hr 2 min) should display 62 minutes.
"""

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + (total_minutes // 60)
        total_minutes = total_minutes % 60
        return Time(total_hours, total_minutes)

    def displayTime(self):
        print(f"Time: {self.hours} hour(s) and {self.minutes} minute(s)")

    def displayMinute(self):
        total = self.hours * 60 + self.minutes
        print(f"Total minutes: {total}")

t1 = Time(2, 50)
t2 = Time(1, 20)

t3 = t1.addTime(t2)

t3.displayTime()      
t3.displayMinute()   
