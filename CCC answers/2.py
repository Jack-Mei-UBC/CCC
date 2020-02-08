length = int(input());
list = input().split(" ");
for x in range(0,len(list)):
    list[x]=int(list[x])
list.sort();
list1 = []
for x in range((length+1)//2):
    list1+=[int(list[x])];
list2 = []
for x in range(length//2):
    list2+=[int(list[x+length//2])];
list2.sort();
list1.sort(reverse=True);
out = [];
for x in range(length//2):
    out+=[list1[x]]
    out+=[list2[x]]
if (length%2 == 1):
    out+=[list1[-1]];
a=""
for x in range (length):
    a+=str(out[x])+" "
a=a[0:len(a)-1]
print(a)
