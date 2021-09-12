class Hw1Q1:
    @staticmethod
    def timeConvert(input_second):
        secdict = [0,0,0,0]
        secdict[2] = input_second // 60
        secdict[3] = input_second % 60
        secdict[1] = secdict[2] // 60
        secdict[2] = secdict[2] % 60
        secdict[0] = secdict[1] // 24
        secdict[1] = secdict[1] % 24
        days=""
        hrs=""
        mins=""
        secs=""

        if secdict[0]!=0:
            if secdict[0]>1:
                days= str(secdict[0])+" days"
            elif secdict[0]==1:
                days= str(secdict[0]) + " day"
        if secdict[1]!=0:
            if secdict[0]!=0:
                hrs = ", "
            if secdict[1]>1:
                hrs= hrs+str(secdict[1])+" hours"
            elif secdict[1]==1:
                hrs= hrs+str(secdict[1]) + " hour"
        if secdict[2]!=0:
            if secdict[0]!=0 or secdict[1]!=0:
                mins = ", "
            if secdict[2]>1:
                mins= mins + str(secdict[2])+" minutes"
            elif secdict[2]==1:
                mins= mins + str(secdict[2]) + " minute"
        if secdict[3]!=0:
            if secdict[0]!=0 or secdict[1]!=0 or secdict[2]!=0:
                secs = ", "
            if secdict[3]>1:
                secs= secs + str(secdict[3])+" seconds"
            elif secdict[3]==1:
                secs= secs + str(secdict[3]) + " second"

        return days+hrs+mins+secs

