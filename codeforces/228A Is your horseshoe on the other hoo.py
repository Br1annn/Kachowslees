#228A Is your horseshoe on the other hoof?

#check how many horseshoes Vela needs that are different(4)

z,x,y,g = input().split()

count = 0

for i in range(0,3):
    if z == x or z==y or z==g:
        count = count + 1
    elif x == y or x == g:
        count = count + 1
    elif y == g:
        count = count + 1
        i+1
    print(count)

print(count)
