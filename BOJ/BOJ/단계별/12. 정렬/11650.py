import sys

t = int(sys.stdin.readline())
ls = []
for i in range(t):
    ls.append(list(map(int, sys.stdin.readline().split())))

ls.sort(key=lambda x: (x[0], x[1]))

for i in range(t):
    print(ls[i][0], ls[i][1])
