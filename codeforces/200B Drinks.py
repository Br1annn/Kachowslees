#200B Drinks

#calculate equal parts orange juice for a drink for Vasya

# #of things in the fridge that are orange juice
x = int(input())

#volume of orange juice in drink
y = list(map(int,input().split()))

sum = 0

for i in y:
    sum = sum + i 

print(sum/ x)
