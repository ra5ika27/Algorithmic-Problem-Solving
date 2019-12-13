# cook your dish here
def main():
    t = int(input())
    for i in range(1, t + 1):
        n, row0, row1 = int(input()), input(), input()
        snakes0, snakes1 = 0, 0
        for i in range(0, n):
            if row0[i] == '*':
                snakes0 += 1
            if row1[i] == '*':
                snakes1 += 1
    print(build_walls(snakes0, snakes1, row0, row1, n))


def build_walls(snakes0, snakes1, row0, row1, n):
    if snakes0 > 0 and snakes1 > 0:
        walls = 1
        count_rows0 = 0
        count_rows1 = 0
        i = 0
        while i < n:
            if row0[i] == '*':
                count_rows0 += 1
            if row1[i] == '*':
                count_rows1 += 1

            if count_rows0 > 1 or count_rows1 > 1:
                i -= 1
                walls += 1
                count_rows0 = 0
                count_rows1 = 0
            i += 1

    elif (snakes0 > 0 and snakes1 == 0) or (snakes0 == 0 and snakes1 > 0):
        walls = max(snakes0, snakes1) - 1
    else:
        walls = 0

    return walls


if __name__ == '__main__':
    main()
