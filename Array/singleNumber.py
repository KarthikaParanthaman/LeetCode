class Solution:
    def singleNumber(self, nums):
        nums = sorted(nums)
        print(nums)
        n = len(nums)

        i = 0
        while i < n:
            j = i+1
            print(i,j)
            if j < n:
                if nums[i] != nums[j]:
                    return nums[i]
            else:
                return nums[i]
            i += 2
            
s = Solution()
nums = [1]
print(s.singleNumber(nums))
        