class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i-nums[i])
        return res 

        # time complexcity space complexity  0(1) and 0(2n )