class Solution:
    def twosum(self, nums, target):
        dict = {}
        result = []
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if x in dict:
                result.append(i) # y index
                result.append(dict[x])
                return result
            else:
                dict[y] = i # y -> x index
        #print(dict)

s = Solution()
print(s.twosum([2,5,4,3,9],6))
        
