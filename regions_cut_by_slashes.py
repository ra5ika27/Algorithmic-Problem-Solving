class DSU(object):
    def __init__(self, N):
        self.parent = [ i for i in range(N)]

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        unique_x = self.find(x)
        unique_y = self.find(y)
        self.parent[unique_x] = unique_y
