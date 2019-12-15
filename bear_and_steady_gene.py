from collections import Counter

n = int(input())
m = n // 4
s = input()
cnt = {'G': 0, 'A': 0, 'C': 0, 'T': 0}
cnt.update(Counter(s))

if all(map(lambda x: x == m, cnt.values())):
    print(0)
    exit()

low, high = 0, n
while high - low > 1:
    mid = (high + low) // 2
    cnt_tmp = dict(cnt)
    for i in range(mid):
        cnt_tmp[s[i]] -= 1
    if all(map(lambda x: x <= m, cnt_tmp.values())):
        high = mid
        continue
    for i in range(mid, n):
        cnt_tmp[s[i - mid]] += 1
        cnt_tmp[s[i]] -= 1
        if all(map(lambda x: x <= m, cnt_tmp.values())):
            high = mid
            break
    else:
        low = mid
print(high)