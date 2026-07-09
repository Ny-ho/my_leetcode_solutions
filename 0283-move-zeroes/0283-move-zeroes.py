class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        count=0
        for i in range (n-1,-1,-1):
            if nums[i]==0:
                nums.pop(i)
                count=count+1

        for i in range(0,count):
            nums.append(0)
        