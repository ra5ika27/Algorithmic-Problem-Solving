rem = []
s = input().strip()
ch = []
for i in range(26):
    ch.append(0)
for i in range(len(s)):
    ch[ord(s[i]) - 97] += 1

set = set()
for i in range(26):
    set.update(ch)
set.discard(0)

for s in set:
    remove = 0
    for c in ch:
        if c > 0:
            if c > s:
                remove += c - s
            elif c < s:
                remove += c
    rem.append(remove)

if min(rem) <= 1:
    print("YES")
else:
    print("NO")
