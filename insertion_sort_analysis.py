def merge_sort(data, low, high):
    if low >= high:
        return 0

    middle = (low + high) / 2

    # recurse to left and right
    left_count = merge_sort(data, low, middle)
    right_count = merge_sort(data, middle + 1, high)

    count = left_count + right_count

    res = []
    i, j = low, middle + 1
    while i <= middle and j <= high:
        if data[i] < data[j]:
            res.append(data[i])
            i += 1
        elif data[i] > data[j]:
            count += middle - i + 1
            res.append(data[j])
            j += 1
        else:
            res.append(data[i])
            i += 1

    while i <= middle:
        res.append(data[i])
        i += 1
    while j <= high:
        res.append(data[j])
        j += 1
    for i in xrange(low, high + 1):
        data[i] = res[i - low]

    return count


def main():
    t = int(raw_input())
    for _ in xrange(t):
        n = int(raw_input())
        data = map(int, raw_input().split())
        print merge_sort(data, 0, n - 1)


if __name__ == '__main__':
    main()