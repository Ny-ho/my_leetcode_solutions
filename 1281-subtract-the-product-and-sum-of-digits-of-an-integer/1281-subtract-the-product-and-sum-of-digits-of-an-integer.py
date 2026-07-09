class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        b=str(n)
        a=len(b)
        product=1
        sums=0
        for i in range(0,a):
            digit1=n%10
            n=n//10
            product=product*digit1
            sums=sums+digit1
        answer=product-sums
        return answer

        
        