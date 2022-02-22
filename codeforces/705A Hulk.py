#705A Hulk

#check to see if hulk likes hates or kinda hates something

x = int(input())
evenFeeling = 'I love'
oddFeeling = 'I hate'
result = 'I hate'
p = 0
if x == 1:
    print(result + ' it')

else:
    for i in range(x-1):
        if p == 0:
            p = 1
            result += ' that ' + evenFeeling
        else:
            p = 0
            result += ' that ' + oddFeeling
    result += ' it'

    print(result) 