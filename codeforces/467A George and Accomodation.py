#467A George and Accomodation

#George wants to live in the same room as his friend Alex
#Check how many open rooms there are


n = int(input())

count = 0

for i in range(n):
    p,q = list(map(int,input().split()))
    if p < q and q-p >= 2:
        count+=1
    
print(count)

