class Solution:
    def movezeroes(self, a):
        i = 0
        j = i + 1
        n = len(a)
        zeroes = []
        while i < n :
            if a[i] == 0 :
                zeroes.append(i)
            i += 1

        zcount = len(zeroes)
        j = zcount-1
        while j >= 0:
            a.pop(zeroes[j])
            a.append(0)
            j -= 1
            
s = Solution()
list = [0,1,0,13,2,4]
s.movezeroes(list)
print(list)

