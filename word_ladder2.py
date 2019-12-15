import collections


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def dfs(word,temp,res):
            temp.append(word)
            if word == endWord:
                res.append(list(temp))
                temp.pop()
                return
            if word in graph:
                for i in graph[word]:
                    if distance[i] == distance[word]+1:
                        dfs(i,temp,res)
            temp.pop()

        words = set(wordList)
        if endWord not in words:
            return []
        letters = 'abcdefghijklmnopqrstuvwxyz'
        queue = collections.deque([(beginWord, 0)])
        distance = {}
        graph = collections.defaultdict(set)
        visited = set([beginWord])


        def bfs(temp,res):
            while queue:
                ind, d = queue.popleft()
                distance[ind] = d
                for i in range(len(ind)):
                    for letter in letters:
                        if letter != ind[i]:
                            new = ind[:i]+letter+ind[i+1:]
                            if new in words:
                                graph[ind].add(new)
                                graph[new].add(ind)
                                if new not in visited:
                                    queue.append((new, d+1))
                                    visited.add(new)
            if endWord not in distance:
                return []

            dfs(beginWord,temp,res)
            return res

        temp = []
        res =[]
        return bfs(temp,res)