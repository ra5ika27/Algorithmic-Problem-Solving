def findItinerary(tickets):
    graph_dict = {}
    # construct the graph
    for ticket in tickets:
        if ticket[0] not in graph_dict:
            graph_dict[ticket[0]] = [ticket[1]]
        else:
            graph_dict[ticket[0]].append(ticket[1])

    # sort the destinations
    for k, v in graph_dict.items():
        graph_dict[k].sort()

    print(graph_dict)

    def dfs(source, result):

        if len(result) == len(tickets) + 1:
            return result

        for index, destination in enumerate(graph_dict[source]):
            print(destination)
            graph_dict[source].pop(index)
            ret = dfs(destination, result + [destination])
            if ret != None:
                return ret
            graph_dict[source].insert(index, destination)

    return dfs("JFK", ["JFK"])


_list = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
print(findItinerary(_list))
