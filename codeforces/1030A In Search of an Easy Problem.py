#1030A In Search of an Easy Problem

#check to see if a certain problem is easy or hard

#number of people in a test
x = int(input())

#if 0 = easy if 1 = hard
peeps = list(map(int,input().split()))
count = 0 
for i in str(peeps):
    if i == '1':
        count = count + 1
if count > 0:
    print("HARD")
else:
    print ("EASY")



