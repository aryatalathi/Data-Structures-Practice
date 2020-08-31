class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i=0
        nums.sort()
        while(i<=len(nums)-2):
            if(nums[i]==nums[i+1]):
                i=i+2
            else:
                return nums[i]
                break
        return nums[len(nums)-1]
        