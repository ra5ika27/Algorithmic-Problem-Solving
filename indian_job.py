if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        N, G = list(map(int, sys.stdin.readline().split()))
        A = list(map(int, sys.stdin.readline().split()))

        if sum(A) > 2 * G:
            print('NO')

        else:
            S = [[0] * (G + 1) for _ in range(N + 1)]

            for i in range(1, N + 1):
                for w in range(1, G + 1):
                    if A[i - 1] > w:
                        S[i][w] = S[i - 1][w]
                    else:
                        S[i][w] = max(S[i - 1][w], S[i - 1][w - A[i - 1]] + A[i - 1])

            if sum(A) - S[N][G] <= G:
                print('YES')
            else:
                print('NO')




