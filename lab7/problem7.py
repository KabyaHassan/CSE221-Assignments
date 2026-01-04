import heapq
import sys
input = sys.stdin.readline

N, E, S, D = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

INF = 10**18
dist1 = [INF] * (N + 1)
dist2 = [INF] * (N + 1)

dist1[S] = 0
pq = [(0, S)]

while pq:
    d, u = heapq.heappop(pq)
    for v, w in graph[u]:
        new_dist = d + w
        if new_dist < dist1[v]:
            dist2[v] = dist1[v]
            dist1[v] = new_dist
            heapq.heappush(pq, (dist1[v], v))
        elif dist1[v] < new_dist < dist2[v]:
            dist2[v] = new_dist
            heapq.heappush(pq, (dist2[v], v))

print(-1 if dist2[D] == INF else dist2[D])
