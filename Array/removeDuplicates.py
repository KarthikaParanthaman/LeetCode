def removeDuplicates(data):
    n = len(data)
    if n <= 1:
        return(n)
    i = j = 1
    while i < n:
        if data[i] != data[i-1]:
            data[j] = data[i]
            j += 1
        i += 1
    return j
                
print(removeDuplicates([0,1,2,2,3]))
    
        