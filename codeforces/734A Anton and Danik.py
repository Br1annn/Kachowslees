#734A Anton and Danik

#check who won chess

n = int(input())

a_count = 0
d_count = 0

chess = input().split()

for i in str(chess):
    if i == 'A':
        a_count = a_count + 1
    elif i == 'D':
        d_count = d_count +1

if a_count > d_count:
    print("Anton")
elif d_count > a_count:
    print("Danik")
elif d_count == a_count:
    print("Friendship")

    
