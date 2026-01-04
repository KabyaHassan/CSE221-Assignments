import sys
import heapq

input = sys.stdin.readline
INF = 10**18

n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))

dist = [INF] * (n + 1)
dist[1] = 0

pq = [(0, 1)]

while pq:
    cd, x = heapq.heappop(pq)
    if cd > dist[x]:
        continue

    for y, wt in g[x]:
        nd = max(cd, wt)
        if nd < dist[y]:
            dist[y] = nd
            heapq.heappush(pq, (nd, y))

ans = []
for i in range(1, n + 1):
    if dist[i] == INF:
        ans.append(-1)
    else:
        ans.append(dist[i])

print(*ans)
