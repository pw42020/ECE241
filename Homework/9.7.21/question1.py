class Hw1Q1():
    @staticmethod
    def timeConvert(input_second):
        min = input_second // 60
        sec = input_second % 60
        hour = min // 60
        min = min % 60
        day = hour // 24
        hour = hour % 24
        if day != 0:
            print(day, "days,", hour, "hours,", min, "minutes,", sec, "seconds")
        if day == 0 and hour != 0:
            print(hour, "hours,", min, "minutes,", sec, "seconds")
        if day == 0 and hour == 0 and min != 0:
            print(min, "minutes,", sec, "seconds")
        if day == 0 and hour == 0 and min == 0:
            print(sec, "seconds")


if __name__ == "__main__":
    input_second = int(input("Input seconds: "))
    Hw1Q1.timeConvert(input_second)
