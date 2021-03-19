#!/usr/bin/python3
from datetime import datetime
import time


class Habit():
    id = 0

    def __init__(self, name, location, time):
        self.name = name
        self.location = location
        self.time = str(time)
        self.count = 0
        Habit.id += 1
        self.id = Habit.id
        self.done = "PRESS"
        self.disable = ""
        self.date = datetime.today()

    def addCount(self):
        self.count += 1

    def subtractCount(self):
        self.count -= 1

    def press(self):
        if self.count > 0:
            self.done = "DONE!"
            self.disable = "disabled"

    def refresh(self):
        return datetime.today()


# obj = Habit("Bryan", "room", 12)
# date = obj.date
# print(date)
# time.sleep(1)
# date1 = obj.refresh()
# print(date1)
# print(date1 - date)
# date3 = datetime.today().isoformat()
# print(date3, type(date3))
# string = datetime.strptime(
#     "2021-03-17T02:45:57.683086", "%Y-%m-%dT%H:%M:%S.%f")
# print(type(string), string)
# delta = string - date
# print(type(string - date), delta)
# obj1 = Habit("Bryan", "room", 13)
# print(obj1.__dict__)
