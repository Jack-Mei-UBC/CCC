J = int(input())
A = int(input())

size = []
for x in range(J):
    size+=[input()]
out = 0

for x in range(A):
    line = input()
    num = int(line[2:])-1
    if (size[num]!="x"):
        if (line[0]=="S"):
            size[num]="x"
            out+=1
        if (line[0]=="M"):
            if (size[num]=="M" or size[num]=="L"):
                size[num]="x"
                out+=1
        if (line[0]=="L"):
            if(size[num]=="L"):
                size[num]="x"
                out+=1
print(out)
