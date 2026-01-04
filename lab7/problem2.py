import sys
import heapq

input = sys.stdin.readline
INF = 10**18

n, m, s, t = map(int, input().split())

g = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))

ds = [INF] * (n + 1)
dt = [INF] * (n + 1)

# Alice
ds[s] = 0
pq = [(0, s)]

while pq:
    cd, x = heapq.heappop(pq)
    if cd > ds[x]:
        continue
    for y, wt in g[x]:
        if ds[y] > cd + wt:
            ds[y] = cd + wt
            heapq.heappush(pq, (ds[y], y))

# Bob
dt[t] = 0
pq = [(0, t)]

while pq:
    cd, x = heapq.heappop(pq)
    if cd > dt[x]:
        continue
    for y, wt in g[x]:
        if dt[y] > cd + wt:
            dt[y] = cd + wt
            heapq.heappush(pq, (dt[y], y))

ans = INF
node = -1

for i in range(1, n + 1):
    if ds[i] != INF and dt[i] != INF:
        cur = max(ds[i], dt[i])
        if cur < ans or (cur == ans and i < node):
            ans = cur
            node = i

if node == -1:
    print(-1)
else:
    print(ans, node)
