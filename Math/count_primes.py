import math
# list prime till n
n = 10
primes = [True] * n

i=2
while i*i < n:
    if primes[i]:
        j=i
        while j*i < n:
            primes[i*j] = False
            j += 1
    i += 1

count = 0 
for i in range(2,n):
    if primes[i]:
        #print(i+1)
        count += 1
print(count)

