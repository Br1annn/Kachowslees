#59A Words

#check how many upper and lowercase letters then print all as lowercase or uppercase

s = input()

uppercase = int(sum(1 for c in s if c.isupper()))
lowercase = int(sum(1 for c in s if c.islower()))

if (uppercase > lowercase):
    print(s.upper())
else:
    print(s.lower())