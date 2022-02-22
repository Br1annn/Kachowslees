#41A Translation

#check to see if something is spelled backwards 

s = input()
t = input()

string = len(s)
reverseString = s[string::-1]

if reverseString == t:
    print("YES")

else:
    print("NO")





