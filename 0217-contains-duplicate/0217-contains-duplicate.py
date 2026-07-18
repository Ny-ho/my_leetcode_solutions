class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        s=set()
        for i in range (0,n):
            s.add(nums[i])
        a=len(s)
        if n==a:
            return False
        else:
            return True