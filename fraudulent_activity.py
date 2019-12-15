def find_fraud(start, end, days_spending, median):
    if median[start] == days_spending:
        return start
    if median[end] == days_spending:
        return end
    if start == end or start + 1 == end:
        return end

    if median[int((start + end) / 2)] <= days_spending:
        return find_fraud(int((start + end) / 2), end, days_spending, median)
    else:
        return find_fraud(start, int((start + end) / 2), days_spending, median)

def main():
    n, days = input().strip().split(' ')
    n, days = [int(n), int(days)]
    spending = [int(i) for i in input().strip().split(' ')]
    notification = 0

    median = spending[:days]
    median.sort()
    for i in range(days, n):
        if days % 2 == 1:
            m = median[int(days / 2)] * 2
        else:
            m = median[int(days / 2)] + median[int(days / 2) - 1]

        if spending[i] >= m:
            notification += 1
        del median[find_fraud(0, days - 1, spending[i - days], median)]
        median.insert(find_fraud(0, days - 2, spending[i], median) + 1, spending[i])
    print(notification)

if __name__ == '__main__':
    main()
