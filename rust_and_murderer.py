T = int(input())


def bfs(graph, start, citiesLen):
    queue = [(start, 0)]

    notvisited = set((x for x in range(1, citiesLen + 1)))
    cities = ['0' for x in range(citiesLen + 1)]
    i = 0
    c = 1
    while i < len(queue):
        (vertex, depth) = queue[i]
        notvisited.discard(vertex)
        visited = set()
        for next in notvisited:
            if (cities[next] == '0' and next not in graph[vertex]):
                cities[next] = str(depth + 1)
                visited.add(next)
                c += 1
                queue.append((next, depth + 1))
        notvisited = notvisited - visited
        i += 1
        if (c == citiesLen + 1):
            break

    return cities[1:start] + cities[start + 1:]


for case in range(T):
    cities, roads = [int(x) for x in input().split()]
    graph = [0]
    for c in range(1, cities + 1):
        graph.append(set())

    for r in range(roads):
        x, y = map(int, input().split())

        graph[x].add(y)

        graph[y].add(x)
    start = int(input())
    res = []
    print(' '.join(bfs(graph, start, cities)))

