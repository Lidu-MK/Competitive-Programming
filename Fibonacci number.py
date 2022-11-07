class Solution:
    def fib(self, num):
        x ={0:0,1:1}
        def fib(num):
            if num in x:
                return x[num]
            else:
                ans=fib(num-1) + fib(num-2)
                x[num]=ans
                return ans

        return (fib(num))
