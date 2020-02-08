b = []
on = 0
total=0;
max = int(input())
for x in range(int(input())):
    if (on > 3):
        total-=b.pop(0)
    inp = int(input())
    b.append(inp)
    total +=inp
    if (total > max):
        break
    on+=1
print(on)
