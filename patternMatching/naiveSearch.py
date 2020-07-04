text = "AABAACAADAABAABA"
pat = "AABA"

n = len(text)
m = len(pat)
print(n, m)
for i in range(0, n - m + 1):
    found = 0
    for j in range(0, m):
        if pat[j] != text[i + j]:
            break
    if j== m-1:
        print(i)
