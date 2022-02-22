#waytoolongwords800

#first and last letter + middle is number of letters
#>10 letters

n = int(input())
# loop 4 (number) times
for i in range(0, n):
    # get input every time in loop
    word = input()
    # eval
    if len(word) > 10:
        between = (len(word)-2)
        first, last = (word[0], word[-1])
        print(f"{first}{between}{last}")
    else:
        print(word)

        




