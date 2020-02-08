num = int(input())
name=[]
specs=[]
for k in range(num):
    info = input().split()
    name+=info[0]
    specs+=[2*int(info[1])+3*int(info[2])+int(info[3])]

if (num >=1 ):
    high1="ZZZZZZZZZZZZZZZ"
    high2="ZZZZZZZZZZZZZZZ"
    y1= 0
    y2 = 0
    x1=0
    x2=0
    for (k in range(num)):
        if(specs[k]>y1):
            high2=high1
            x2=x1
            y2=y1
            high1=name[k]
        elif(specs[k]==y1):
            if(name[k]<high1):
                high2=high1
                x2=x1
                y2=y1
                high1=name[k]
