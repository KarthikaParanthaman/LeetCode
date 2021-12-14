def generate(numRows):
        i = 0
        a = [0] * numRows 
        while i < numRows:
            # create list
            a[i] = [0] * (i+1)
            
            # assign start and end
            a[i][0] = 1
            a[i][i] = 1
                
            j = 1
                
            while j <= i-1 :
                print(i, j)
                if j-1 >= 0 and i-1 >= 0:
                    a[i][j] += a[i-1][j-1]
                    
                if i-1 >= 0:
                    a[i][j] += a[i-1][j]
            
                j += 1
            i += 1
               
        print(a)    
generate(5)

# a = [0] *5
# for i in range(5):
#     a[i] = [0]*(i+1)
# print(a)
                
                