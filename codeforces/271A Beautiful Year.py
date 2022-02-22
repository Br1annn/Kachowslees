#271A Beautiful Year

#check for distinct numbered year and has to be larger than the current 

y = int(input())

while True:
    y = y+1
    if len(set(str(y))) == len(str(y)):
        break
print(y)
