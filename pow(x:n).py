class Solution:
    base = float
    power = int
    def myPow(self, base,power):
        if power ==0:
            return 1
        if power ==1:
            return base
        if power ==0:
            return 0
        if power ==1:
            return 1
        if power <0:
            return 1/self.myPow(base,-power)
        
        if power %2:
            return base*self.myPow(base,power-1)
        else:
            return self.myPow(base*base, power//2)
        
