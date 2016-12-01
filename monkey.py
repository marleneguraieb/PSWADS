import random

def generateOne(strlen):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    res = ''
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res
print (generateOne(28))

def score(goal,teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame = numSame+1
    return numSame/len(goal)



# def main():
#     goalstring = 'methinks it is like a weasel'
#     newstring = generateOne(28)
#     best = 0
#     newscore = score(goalstring,newstring)
#     i = 0
#     while newscore<1:
#         i = i + 1
#         if i%1000000 == 0:
#             print(i)
#         if newscore > best:
#             print (newscore,newstring)
#             best = newscore
#         newstring = generateOne(28)
#         newscore = score(goalstring,newstring)
 
def main():
    goalstring = 'methinks it is like a weasel'
    newstring = generateOne(28)
    best = 0
    newscore = score(goalstring,newstring)
    i = 0
    while newscore<=1:
        i = i + 1
        if i%1000000 == 0 and newstring != goalstring:
            print(i)
        if newscore > best:
            print (newscore,newstring)
            best = newscore
        newstring = ''.join([goalstring[i] if goalstring[i] == newstring[i] else generateOne(28)[i] for i in range(len(newstring))])
        newscore = score(goalstring,newstring)
        
        
main()
