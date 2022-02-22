#723A The New Year: Meeting Friends

#min distance to travel for all 3 friends

x = list(map(int, input().split()))

x.sort()

print(x[-1] - x[0])