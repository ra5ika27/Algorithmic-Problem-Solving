def main(N,H,I):
    people = [[0] * N for _ in range(H + 1)]
    for n in range(N):
        a = [int(x) for x in input().split()]
        for h in a[1:]:
            people[h][n] += 1

    apartments = [(0, 1)]
    S = [[0] * N for _ in range(H + 1)]
    for h in range(1, H + 1):
        for n in range(N):
            if h - I > 0 and S[h - 1][n] < apartments[h - I][0]:
                S[h][n] = people[h][n] + S[h - I][apartments[h - I][1]]

            else:
                S[h][n] = people[h][n] + S[h - 1][n]

        apartments.append(max((m, i) for i, m in enumerate(S[h])))

    print(max(S[-1]))

if __name__ == '__main__':
    N, H, I = [int(x) for x in input().split()]
    main(N,H,I)