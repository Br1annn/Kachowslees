#339A Helpful Maths

#add numbers together 1,2,3 only, in numeric order

#splits plus sign
numbers = input().split('+')

#sort numbers lowest to highest
numbers.sort()

exit = ''

for i in numbers:
    exit = exit + i + '+'

print(exit[:-1])