list = []
lenth = int(input())
for x in range(lenth):
    k = int(input())
    if (k==0):
        list.pop()
    else:
        list+=[k]
out = 0;
while (len(list) > 0):
    out+=list.pop()
print(out)
