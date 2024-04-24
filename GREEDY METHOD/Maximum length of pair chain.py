class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pair.sort(key=lambda x:x[1])
        count=1
        prev_end=pairs[0][1]
        i=1
        while i<len(pairs):
            if pairs[i][0]>prev_end:
                count+=1
                prev_end=pairs[i]
        
