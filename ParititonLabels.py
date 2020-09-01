class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        map1={}
        for i in range(0,len(S)):
            map1[S[i]]=i
        end=0
        start=0
        result=[]
        for i in range(0,len(S)):
            c=S[i]
            end=max(end,map1.get(c))
            if i==end:
                result.append(end-start+1)
                start=end+1
        return result
        
#Time complexity is O(2n), one pass to create a hashmap, second pass is to move two pointers
#Space complexity is O(1)
