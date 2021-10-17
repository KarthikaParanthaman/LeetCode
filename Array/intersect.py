class Solution:
    def traverse(self, nums1,nums2):
        l =[]
        i = 0 # nums1 index
        j = 0 # nums2 index
#        print(nums1,nums2)
        while i < len(nums1) and j < len(nums2):
 #           print(i,j)
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                l.append(nums1[i])
                i += 1
                j += 1
            else:
                j += 1
        return l




    def intersect(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        if(l1 < l2):
            return self.traverse(nums1,nums2)
        else:
            return self.traverse(nums2,nums1)
        

s = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(s.intersect(nums1, nums2))