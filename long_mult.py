# long hand multiplication
# originally inspired by reading about this being an interview question

def long_mult(x,y):
    xStr = str(x)
    yStr = str(y)

    # create lists in order to store the ones digits that are calculated (represents rows to be added in hand calculations)
    aList = []
    for letters in yStr:
        aList.append([])

    # loop through the different integers for the calculation
    for ydig in range(len(yStr)-1,-1,-1):
        store = 0
        for xdig in range(len(xStr)-1,-1,-1):

            # calculate each integer multiplied together, 
            calc = str(int(xStr[xdig])*int(yStr[ydig]) + store)
            if xdig == 0:
                aList[ydig].append(calc)
                continue

            # if the integer is greater than 9 then store the tens place and carry over to the next calculation
            if len(calc) > 1:
                aList[ydig].append(calc[-1])
                store = int(calc[0])
            else:
                aList[ydig].append(calc)

    # numbers in the lists are reversed
    reverse_a = aList[::-1]
    total = 0

    # summing the integers together and also adding the necessary place holder zeros as in hand calculation
    for row in range(len(aList)):
        total += int(''.join(reverse_a[row][::-1]) + ('0'*row))
    return total
