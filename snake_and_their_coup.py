for i in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    count = 0
    if (a.count('*') >= 1 and b.count('*') >= 1):
        count = 1
    py = 0
    for j in range(n):
        if ((py == 1 and a[j] == '*') or (py == 2 and b[j] == '*') or (py == 3 and (a[j] == '*' or b[j] == '*'))):
            count += 1
        if (a[j] == '*' and b[j] == '*'):
            py = 3
        else:
            if (a[j] == '*'):
                if (py == 2):
                    py = 3
                else:
                    py = 1
            if (b[j] == '*'):
                if (py == 1):
                    py = 3
                else:
                    py = 2
    print(count)
