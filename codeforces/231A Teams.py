#231A teams codeforces

#number of tests(integer)
n = int(input())
count = 0

#3 friends solutions, if 1 = correct if 0 != idk
for i in range (0,n):

    x=input()
    if x.count('1') >=2:
        count +=1

print(count)







