def main():
    z = input().split()
    hull = int(zzz[0])
    islands = int(zzz[1])
    routes = int(zzz[2])

    graph = [[]for i in range(islands+1)]#creating map

    for x in range(routes):
        z = input().split()
        graph[z[0].append([z[1],z[2],z[3]])]#adding paths
        graph[z[1].append([z[0],z[2],z[3]])]#^^^
    z = input().split()
    start = z[0]
    end = z[1]


main()
