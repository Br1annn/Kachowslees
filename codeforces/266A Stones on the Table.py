#266A Stones on the Table

#check if stones are same colors next to each other and add numbers

#number of stones
n = int(input())
count = 0
stones = input()
for i in range(1,n):
    if stones[i] == stones[i-1]:
        count +=1

print(count)

