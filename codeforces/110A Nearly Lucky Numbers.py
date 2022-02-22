#110A Nearly Lucky Numbers

#check if all numbers are 4 and or 7

n = input()

c = 0

#check how many 4s and 7s in the input
for i in n:
    if i == '4' or i == '7':
        c+=1

count = 0
#check if its a 4 or 7 in the count string
for i in str(c):
    if i == '4' or i == '7':
        count+=1

#check to make sure 4 or 7 is the length of the input
if count == len(str(c)):
    print("YES")
else:
    print("NO")
