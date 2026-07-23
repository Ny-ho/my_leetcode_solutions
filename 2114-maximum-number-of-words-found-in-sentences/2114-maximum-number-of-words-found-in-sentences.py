class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        n=len(sentences)
        max=0
        for i in range(0,n):
            a=sentences[i]
            count=a.count(" ")
            if count>max:
                max=count




        return max+1
        