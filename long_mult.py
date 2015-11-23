# long hand multiplication
# originally inspired by reading about this being an interview question

def long_mult(x,y):
    xStr = str(x)
    yStr = str(y)
    aList = []
    for letters in yStr:
        aList.append([])
    for ydig in range(len(yStr)-1,-1,-1):
        store = 0
        for xdig in range(len(xStr)-1,-1,-1):
            calc = str(int(xStr[xdig])*int(yStr[ydig]) + store)
            if xdig == 0:
                aList[ydig].append(calc)
                continue
            if len(calc) > 1:
                aList[ydig].append(calc[-1])
                store = int(calc[0])
            else:
                aList[ydig].append(calc)
    reverse_a = aList[::-1]
    total = 0
    for row in range(len(aList)):
        total += int(''.join(reverse_a[row][::-1]) + ('0'*row))
    return total
