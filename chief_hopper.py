from math import ceil
def energy(arr):
    s, p = 0, 2.0
    for i in range(len(arr)):
        s += arr[i] / p
        p *= 2

    attempt = int(ceil(s))

    print(s)
    # floating points are super tricky.
    # so sometimes the answer can be of by 1
    # arr = [2] * 100 + [100]
    start = attempt
    for i in arr:
        start = 2 * start - i
        if start < 0:
            attempt += 1
            break

    return attempt


#arr = [2] * 100000 + [4]
arr = [2,3,4,3,2]
print (energy(arr))