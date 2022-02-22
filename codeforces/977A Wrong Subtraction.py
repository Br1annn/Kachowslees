#977A Wrong Subtraction

#if the last digit of the number is zero, she divides the number by 10 (i.e. removes the last digit).
#if the last digit of the number is non-zero, she decreases the number by one;

n = list(map(int,input().split()))

for i in range(0,n[1]):

    if(n[0] % 10 == 0):
        n[0] = n[0] // 10
    else:
        n[0] = n[0] - 1


print(n[0])
