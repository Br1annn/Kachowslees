#116A Tram

#check number of passengers who get on and off the tram

#number of stops
x = int(input())

array = []

max = 0
person = 0
while x > 0:
    x -= 1
    arraylist = list(map(int,input().split()))
    array.append(arraylist)

for i in array:
    person = person - i[0] + i[1]
    if max < person:
        max = person
print(max)


'''0 + 3 = 3
3 - 2 = 1
1 + 5 = 6
6 - 4 = 2
2 + 2 = 4
4 - 4 = 0'''

