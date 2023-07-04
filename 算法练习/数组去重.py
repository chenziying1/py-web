class Solution:
    def removeDuplicates(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        print (len(nums))


s = Solution()
nums = [1,1,2]
s.removeDuplicates(nums)
