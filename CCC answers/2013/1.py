y = int(input())+1

def comp(num):
    failed = False
    if (len(str(num))<=1):
        return(True)
    for x in range(1,len(str(num))):
        if (str(num)[0] == str(num)[x]):
            failed = True
            break
    if (failed):
        return(False)
    return(comp(str(num)[1:len(str(num))]))

while(True):
    if (not comp(y)):
        y+=1
    else:
        print(y)
        break
