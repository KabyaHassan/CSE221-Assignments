import sys
import heapq

input = sys.stdin.readline
INF = 10**18

n, m, s, d = map(int, input().split())
w = list(map(int, input().split()))

g = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)

dist = [INF] * (n + 1)
dist[s] = w[s - 1]

pq = [(dist[s], s)]

while pq:
    cd, x = heapq.heappop(pq)
    if cd > dist[x]:
        continue

    for y in g[x]:
        nd = cd + w[y - 1]
        if nd < dist[y]:
            dist[y] = nd
            heapq.heappush(pq, (nd, y))

if dist[d] == INF:
    print(-1)
else:
    print(dist[d])

