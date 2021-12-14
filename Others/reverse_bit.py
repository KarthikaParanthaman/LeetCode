def reverse_bit(n):
    r = 0
    while n > 0:
        r = r << 1
        # get last bit of n
        if n & 1:
            r = r | 1 

        n = n >> 1
    return r

print(reverse_bit(0b11111111111111111111111111111101))
                    
            
         