#236A Boy or Girl

#check for odd or even username distinct characters and determine if boy(odd) or girl(even)

#checks for unique characters
username = ''.join(set(input()))

count = 0

for i in range(0,len(username)):
    count+=1
if count%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')






