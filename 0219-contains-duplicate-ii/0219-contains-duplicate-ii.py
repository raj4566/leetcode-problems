class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window =set()
        left =0
    #left is to check the Abs - absolute eq (i-j)<=k.
        for i in nums:
            if i in window:
                return True
            window.add(i)
            if len(window)>k:
                window.remove(nums[left])
                left +=1
        return False