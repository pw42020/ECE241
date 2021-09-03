class Polynomial():
    def parta(a,b,c):
        x=(c-2*b)/a
        print(str(a)+"x+"+str(2*b)+" = "+str(c))
        print("x="+str(x))
    def partb(a,b,c):
        x=(c**2-2*b)/a
        print("sqrt("+str(a)+"x+"+str(2*b)+") = "+str(c))
        print("x="+str(x))



if __name__=="__main__":
    Polynomial.parta(1,1,4)
    Polynomial.partb(1,1,4)