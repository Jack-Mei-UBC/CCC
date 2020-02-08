gates = int(input())
planes = int(input())
filled = [None]*gates

out = 0;
for x in range(planes):
    k = int(input())-1
    for k in range(k,-1,-1):
        if (filled[k]==None):
            filled[k]=1;
            k=-1
            out+=1;
            break;
    if (k == 0):
        break
print(out)
