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
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        friend_circles = 0
        length = len(M)
        dsu = DSU(length)

        for i in range(1, length):
            for j in range(i):
                if M[i][j] == 1:
                    dsu.union(i, j)
        for i in range(len(dsu.parent)):
            if dsu.parent[i] == i:
                friend_circles += 1
        return friend_circles
