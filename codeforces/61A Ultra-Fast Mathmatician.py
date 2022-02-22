#61A Ultra-Fast Mathmatician
import re
#calculate 2 numbers consisting of 1 or 0, if 1 + 1 = 2 -> 0

num1 = input()
num2 = input()

string = []

for i, x in enumerate(num1):
    if x == num2[i]:
        string.append('0')
    else:
        string.append('1')

print("".join(string))

