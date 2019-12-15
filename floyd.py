# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, raw_input().strip().split(' '))
paths = [0] * (N + 1)
for i in xrange(N + 1):
    a = [float('inf')] * (N + 1)
    a[i] = 0
    paths[i] = a

for _ in xrange(M):
    x, y, r = map(int, raw_input().strip().split(' '))
    paths[x][y] = r


def floyd_warshal(paths):
    N = len(paths)
    for k in xrange(1, N):
        for v1 in xrange(1, N):
            for v2 in xrange(1, N):
                new_path = paths[v1][k] + paths[k][v2]
                if paths[v1][v2] > new_path:
                    paths[v1][v2] = new_path


floyd_warshal(paths)
Q = input()
for _ in xrange(Q):
    a, b = map(int, raw_input().strip().split(' '))
    answ = paths[a][b]
    if answ == float('inf'):
        answ = -1
    print answ
