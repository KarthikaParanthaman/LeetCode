class Solution:
    def reverse(self, data, start, stop) :

        while(start < stop):
            tmp = data[start]
            data[start] = data[stop-1]
            data[stop-1] = tmp
            start += 1
            stop -= 1
            
    def rotate(self, data, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.reverse(data,0,len(data))
        self.reverse(data,0,k)
        self.reverse(data,k,len(data))

s = Solution()
data = [1,2]
k = 3
k = k%len(data)
s.rotate(data, k)
print(data)