import sys
import heapq

input = sys.stdin.readline
INF = 10**18

n, m = map(int, input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

g = [[] for _ in range(n + 1)]
for i in range(m):
    g[u[i]].append((v[i], w[i]))

# dist[node][parity]
dist = [[INF, INF] for _ in range(n + 1)]

pq = []

# start: node 1, no previous edge
dist[1][0] = 0
dist[1][1] = 0
pq.append((0, 1, 0))
pq.append((0, 1, 1))

heapq.heapify(pq)

while pq:
    cd, x, p = heapq.heappop(pq)

    if cd > dist[x][p]:
        continue

    for y, wt in g[x]:
        np = wt & 1
        if np == p:
            continue

        nd = cd + wt
        if nd < dist[y][np]:
            dist[y][np] = nd
            heapq.heappush(pq, (nd, y, np))

ans = min(dist[n][0], dist[n][1])

if ans == INF:
    print(-1)
else:
    print(ans)

