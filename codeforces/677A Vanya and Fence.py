#677A Vanya and Fence

#check height of people to not be over the fence

#n is number of people, h is height of fence

n,h = map(int,input().split())
a = list(map(int,input().split()))

sum = 0

for i in range(n):
    if a[i] > h:
        sum = sum + 2
    else:
        sum = sum + 1
print(sum)