# cook your dish here
def main():
    testcases = int(input())
    for _ in range(testcases):
        neighbor_x = [-1, 0, 0, 1]
        neighbor_y = [0, -1, 1, 0]
        N = int(input())
        M, visited = [], []
        for i in range(N):
            m = []
            v = []
            for ch in input():
                m.append(ch)
                v.append(0)
            M.append(m)
            visited.append(v)
        ways = 1
        for i in range(N):
            for j in range(N):
                if M[i][j] != '.':
                    if visited[i][j] == 0:
                        grizzly = brown = polar = question = 0
                        stack = [[i, j]]
                        dfs(M, visited, N, stack, neighbor_x, neighbor_y, grizzly, brown, polar, question)
                        if grizzly > 1:
                            return 0
                        if polar >= 1 and brown >= 1:
                            return 0
                        if ((polar + grizzly + brown) >= 1) and grizzly >= 1:
                            return 0
                        total = polar + question + grizzly + brown
                        if total == question:
                            if total == 1:
                                ways = ways * 3

                            else:
                                ways = ways * 2

                            ways = ways % 1000000007

        print(ways)


def dfs(M, visited, N, stack, neighbor_x, neighbor_y, grizzly, brown, polar, question):
    while len(stack) > 0:
        point = stack.pop()
        i = point[0]
        j = point[1]
        visited[i][j] = 1
        if M[i][j] == '.':
            return
        if M[i][j] == 'G':
            grizzly += 1
        if M[i][j] == 'B':
            brown += 1
        if M[i][j] == 'P':
            polar += 1
        if M[i][j] == '?':
            question += 1

        for k in range(4):
            x = i + neighbor_x[k]
            y = j + neighbor_y[k]

            if x < N and y < N >= 0 and y >= 0 and M[x][y] != '.' and visited[x][y] == 0:
                stack.append([x, y])


if __name__ == '__main__':
    main()
