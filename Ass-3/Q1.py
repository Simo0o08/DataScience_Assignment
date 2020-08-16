# Q1
class Opr:
    a=eval(input())
    b=eval(input())
    def add(self):
        res=self.a+self.b
        print("sum ",res)
    def sub(self):
        res=self.a-self.b
        print("subtraction="res)
    def mul(self):
        res=self.a*self.b
        print("multiplication="res)
    def div(self):
        if(b!=0):
            res=self.a/self.b
            print("divide="res)

A = Opr()
A.add()
A.sub()
A.mul()
A.div()
