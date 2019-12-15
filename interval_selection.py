def interval_selection(N,intervals):
    intervals.sort(key=lambda x:(x[1],x[0]))
    selected = [intervals[i][1] for i in range(N)]
    flag = [1 for i in range(N)]

    for i in range(N):
        count = 0
        for j in range(N):
            if flag[j]:
                if intervals[j][0] <= selected[i] and intervals[j][1] >= selected[i]:
                    count += 1
                    if count > 2:
                        flag[j] = 0

    return sum(flag)


T = int(input())
for _ in range(T):
    N = int(input())
    intervals = [tuple(map(int,input().split())) for i in range(N)]
    print(interval_selection(N,intervals))