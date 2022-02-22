#617A Elephant
import math
#number of steps elephant needs to take from point a to point b
#max 1-5 steps
#ex input 5 = 1 step, input 12 = x2 5 steps and 1 2 step

n = int(input())
steps = 0

steps = n/5
if(n%5==0):
    print(math.ceil(steps))
else:
    print(math.ceil(steps))
