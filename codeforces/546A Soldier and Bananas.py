#546A Soldier and Bananas

#buying bananas for a soldier

#k = dollars per banana, w = amt of bananas he wants, n = his dollars
k,n,w = input().split()

count = 0
w = int(w)
for i in range (1,w+1):
    k = int(k)
    n = int(n)
    count = count + i *k


#subtract total banana by amount of money and ask to borrow x amount

borrow = count - n


if(borrow < 0):
    borrow = 0
print(borrow)
