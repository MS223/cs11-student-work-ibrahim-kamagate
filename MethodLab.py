class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)

    def __add__(self, other):
        # return str(self.hour+other.hour) + ":" + str(self.minute+other.minute) + ":" + str(self.second+other.second)
#I had to use the self and other which is time 1 and time 2
         return Time(self.hour+other.hour, self.minute+other.minute, self.second+other.second)
#     doing it this way is better than the other one becuase it time1 and time2 and add them then it make whatever they equally to self and other is now time3
time1 = Time(5, 32, 0)
time2 = Time(23, 11, 11)
time3 = Time(7, 14, 28)
print time1
print time2

print time1 + time2 + time3
