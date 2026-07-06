class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index=len(s)-1
        count=0
        for index in range(index,-1,-1):
            if s[index] == " ":
                if count>0:
                    return count
            else :
                count=count+1
        return count