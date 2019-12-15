class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(graph, node, cur_itinerary, n):
            if len(cur_itinerary) == n:
                return cur_itinerary

            for index, value in enumerate(graph[node]):
                graph[node].pop(index)
                res = dfs(graph, value, cur_itinerary + [value], n)

                if res is not None:
                    return res
                graph[node].insert(index, value)

        graph = collections.defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])

        for k in graph:
            graph[k].sort()

        n = len(tickets) + 1
        return dfs(graph, "JFK", ["JFK"], n)