class Solution:
    def containsDuplicate(self, nums):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return True
            else:
                d[nums[i]] = 1
        return False

s = Solution()
print(s.containsDuplicate([1,2,4,5,6,7]))
        