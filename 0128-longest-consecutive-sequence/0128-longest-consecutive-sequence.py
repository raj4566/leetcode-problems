class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        result = 0
        for i in res:
            if i-1 not in res:
                count = 1
                num = i+1
                while num in res:
                    count+=1
                    num+=1
                result = max(result,count)
        return result