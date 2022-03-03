from sys import stdin

T = int(stdin.readline())
ans = [1]
mod = 998244353
for i in range(1000005):
    ans.append((ans[i] * (2 * i + 1)) % mod)
for i in range(T):
    N = int(stdin.readline())
    print(ans[N])