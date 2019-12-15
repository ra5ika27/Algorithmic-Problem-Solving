#binary search
def min_clique(N, M):
    low, high = 1, N
    while low + 1 < high:
        mid = (low + high) // 2
        d, r = divmod(N, mid)
        m_max = (N * N - (d + 1) * (d + 1) * r - d * d * (mid - r)) // 2
        if m_max < M:
            low = mid
        else:
            high = mid
    return high


T = int(input())
for t in range(T):
    N, M = [int(x) for x in input().split(' ')]
    print(min_clique(N, M))
