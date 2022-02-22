#486A Calculating function
import math
#calculate positive and negative integers

x = int(input())
n = 0
if (x%2==0):
    n = x/2
else:
    n = ((x+1)/2)*-1

print(math.trunc(n))