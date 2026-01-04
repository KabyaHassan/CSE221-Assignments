import sys
import heapq

input = sys.stdin.readline
INF = 10**18

n, m, s, d = map(int, input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

g = [[] for _ in range(n + 1)]

for i in range(m):
    g[u[i]].append((v[i], w[i]))

dist = [INF] * (n + 1)
par = [-1] * (n + 1)

dist[s] = 0
pq = [(0, s)]

while pq:
    cd, x = heapq.heappop(pq)

    if cd > dist[x]:
        continue

    for y, wt in g[x]:
        if dist[y] > cd + wt:
            dist[y] = cd + wt
            par[y] = x
            heapq.heappush(pq, (dist[y], y))

if dist[d] == INF:
    print(-1)
else:
    path = []
    cur = d
    while cur != -1:
        path.append(cur)
        cur = par[cur]

    path.reverse()
    print(dist[d])
    print(*path)
