numbers = [1,2,3,4,5,6,7,8,9]
alreadyCal = []

def countTheDigits(astr,alist):
    if alist == []:
        return False , []
    for i in astr:
        if int(i) in alist:
            alist.remove(int(i))
        else:
            return False , []
    return True,alist

for firstProd in range(1,10000):
    for secondProd in range(1,10000):
        tempNumber = numbers[:]
        rsult = firstProd*secondProd
        flag,tempNumber = countTheDigits(str(rsult),tempNumber)
        if not flag:
            continue
        flag,tempNumber = countTheDigits(str(firstProd),tempNumber)
        if not flag:
            continue
        flag,tempNumber = countTheDigits(str(secondProd),tempNumber)
        if flag and tempNumber == []:
            if rsult not in alreadyCal:
                alreadyCal.append(rsult)
print(sum(alreadyCal))