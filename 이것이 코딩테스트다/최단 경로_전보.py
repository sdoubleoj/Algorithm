# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#개선된 다익스트라 알고리즘
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 도시(노드) 개수 n, 통로(간선) 개수 m, 메시지를 보내는 도시(시작노드) start
n, m, start = map(int, input().split())
# 노드별 노드 연결 정보 리스트 생성
graph = [[] for _ in range(n+1)]
#최단 거리 테이블(1차원 리스트)
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    # 도시 X에서 다른 도시 Y로 이어지는 통로를 따라 메시지가 전달되는 시간 Z
    x, y, z = map(int, input().split())
    graph[x][y] = z


def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    
    while q: #큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist: #현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #노드i[0]까지의 갈 때, 현재 노드를 거쳐서 이동하는 거리가 다른노드를 거치는 것보다 더 짧은 경우 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

#다익스트라 알고리즘 수행
dijkstra(start)

#도달할 수 있는 노드의 개수
count = 0
#도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    #도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
        
# 도시 C에서 보낸 메시지를 받는 도시의 총 개수 & 총 소요 시간
print(count-1, max_distance) #시작노드는 제외해야 하므로 -1
