#!/bin/python3
MOD = 10 ** 9 + 7

fact = [1]
cur = 1
for i in range(1, 6 * 10 ** 4):
    cur *= i
    cur %= MOD
    fact.append(cur)

alpha = "abcdefghijklmnopqrstuvwxyz"

dp = [0]
dp2 = [[0] * 26]


def bit_manipulation(c):
    return 1 << (alpha.find(c))


def initialize(s):
    cur = 0
    for c in s:
        tmp = [i for i in dp2[-1]]
        tmp[alpha.find(c)] += 1
        cur ^= bit_manipulation(c)
        dp.append(cur)
        dp2.append(tmp)


def modInv(x, pow=MOD - 2):
    if pow <= 3:
        return (x ** pow) % MOD
    else:
        tmp = modInv(x, pow // 2)
        tmp *= tmp
        tmp %= MOD
        if pow % 2 == 0:
            return tmp
        else:
            return (tmp * x) % MOD


mi = [modInv(fact[x]) for x in range(6 * 10 ** 4)]


def answer_query(l, r):
    tmp = dp[l - 1] ^ dp[r]
    tmp2 = [(dp2[r][i] - dp2[l - 1][i]) // 2 for i in range(26)]
    possLetters = 0
    for c in range(26):
        if tmp & (1 << c):
            possLetters += 1
    middle = max(possLetters, 1)
    others = (r - l + 1 - possLetters) // 2
    ans = (fact[others] * middle) % MOD
    for i in tmp2:
        if i > 0:
            ans *= mi[i]
            ans %= MOD
    return ans


if __name__ == "__main__":
    s = input().strip()
    initialize(s)
    q = int(input().strip())
    for a0 in range(q):
        l, r = input().strip().split(' ')
        l, r = [int(l), int(r)]
        result = answer_query(l, r)
        print(result % MOD)