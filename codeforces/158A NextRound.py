#158A NextRound CodeForces

#first value = amount of participants +  space + 2nd value is number over to be accepted
n,k = list(map(int, input().split()))
score_length = list(map(int, input().split()))
count = 0

for i in score_length:
    if i > 0 and i >= score_length[k-1]:
        count+=1





print(count)
        
    

