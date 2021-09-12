class Hw1Q1:
    def timeConvert(input_second):
        min = input_second // 60
        sec = input_second % 60
        hour = min // 60
        min = min % 60
        day = hour // 24
        hour = hour % 24
        if day != 0:
            return str(day)+ " days, "+ str(hour)+ " hours, "+ str(min) + " minutes, "+ str(sec)+ " seconds"
        if day == 0 and hour != 0:
            return str(hour)+ " hours, "+ str(min) + " minutes, "+ str(sec)+ " seconds"
        if day == 0 and hour == 0 and min != 0:
            return str(min) + " minutes, "+ str(sec)+ " seconds"
        if day == 0 and hour == 0 and min == 0:
            return str(sec)+ " seconds"