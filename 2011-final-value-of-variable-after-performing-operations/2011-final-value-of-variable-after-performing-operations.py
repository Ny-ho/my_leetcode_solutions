class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        n=len(operations)
        for i in range(0,n):
            if operations[i] == "++X" or operations[i]=="X++":
                x=x+1
            elif operations[i] =="--X" or operations[i]=="X--":
                x=x-1
        return x
        

        