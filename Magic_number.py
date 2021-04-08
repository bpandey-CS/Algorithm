# Magic number
# 199 = 1+9+9 = (19) = 1+9 = (10) = 1+0 = 1 (here the final result is 1 so Magic)
class Number:
    def __init__(self):
        print("Enter Lower Bound")
        l = int(input())
        print("Enter Upper Bound")
        u = int(input())
        self.lower = l
        self.upper = u

    def sum_of_degits(self, number:int)->int:
        summ = 0
        for digit in str(number):
            summ = summ + eval(digit)
        return summ
    
    def magic(self, number:int)->bool:
        while (number>=10):
            number = self.sum_of_degits(number)
        if number==1:
            return True
        else:
            return False

    def main(self):
        for i in range(self.lower,self.upper+1):
            if self.magic(i):
                print(i)


n = Number()
n.main()
