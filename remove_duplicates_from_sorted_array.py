class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=1
        if(len(nums)==1 or len(nums)==0):
            return len(nums)
        else:
            for j in range(len(nums)-1):
                if(nums[j-1]==nums[j]):
                    nums.pop(j)
                else:
                    j=j+1
        return (len(nums))
