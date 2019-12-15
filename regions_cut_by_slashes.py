class DSU(object):
    def __init__(self, N):
        self.parent = [i for i in range(N)]

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        unique_x = self.find(x)
        unique_y = self.find(y)
        self.parent[unique_x] = unique_y


class Solution(object):
    def regionsBySlashes(self, grid):
        N = len(grid)
        dsu = DSU(4 * N * N)

        for i in range(N):
            for j in range(N):
                if grid[i][j] == "\\":
                    grid[i][j] = '#'

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r * N + c)
                if val in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in '# ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)

                # for top and bottom
                if r + 1 < N:
                    dsu.union(root + 3, (root + 4 * N) + 0)
                if r - 1 >= 0:
                    dsu.union(root + 0, (root - 4 * N) + 3)
                # for left and right
                if c + 1 < N:
                    dsu.union(root + 2, (root + 4) + 1)
                if c - 1 >= 0:
                    dsu.union(root + 1, (root - 4) + 2)

        return sum(dsu.find(x) == x for x in range(4 * N * N))
