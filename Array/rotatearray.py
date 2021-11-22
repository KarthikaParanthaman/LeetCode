class Solution:
    
    def reverserow(self, matrix):
        n = len(matrix)
        i = 0
        j = n-1
        while i < j :
            tmp = matrix[i]
            matrix[i] = matrix[j]
            matrix[j] = tmp
            i += 1
            j -= 1
            
        return matrix
    
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # tranpose
        for i in range(n):
            for j in range(i,n):
                # swap ij ->ji
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
                
        # reverse row element
        for i in range(n):
            matrix[i] = self.reverserow(matrix[i])
        
        print(matrix)


s = Solution()
data = [[1,2],[3,4]]
s.rotate(data)

