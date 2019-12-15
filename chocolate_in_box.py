N = int(input())
A = [int(i) for i in input().split()]

def nim_sum(ar):
    result = 0
    for a in ar:
        result ^= a
    return result

nim_sum = 0
for a in A:
    nim_sum ^= a

count = 0
for a in A:
    nim_sum_tmp = nim_sum ^ a
    if nim_sum_tmp < a:
        count += 1

print(count)