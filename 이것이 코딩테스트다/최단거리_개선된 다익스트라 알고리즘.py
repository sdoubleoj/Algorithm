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
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


n, m = map(int, input().split())
start = int(input())
graph = [ [] for i in range(n+1) ]
distance = [INF] * (n+1)


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append( (b,c) )


'''
개선된 다익스트라에서는 최단 거리가 가장 짧은 노드를 선택하는 과정을
다익스트라 최단 경로 함수 안에서 '우선순위 큐'를 이용하는 방식으로 대체할 수 있으므로,
get_smallest_node() 함수 작성할 필요 없음
'''


def dijstra(start):
    q = []
    
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입(push)
    heapq.heappush(q, (0,start))
    distance[start] = 0
    
    while q: #큐가 비어있지 않다면,
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기(pop) (최소 힙 기반이므로 그냥 꺼내면 됨)
        dist, now = heapq.heappop(q)
        
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        '''
        매 단계마다 연결노드에 대한 최단거리 정보가 우선순위 큐에 저장되는데, 거리가 작은 순서대로 기록되므로
        처리된 적이 있다면,최단거리테이블에 갱신되어 저장된 현재노드까지의 최단거리값이
        큐에서 꺼내온 최단거리값보다 작음
        '''
        if distance[now] < dist: 
            continue
        
        #현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            
            #노드i[0]까지의 갈 때, 현재 노드를 거쳐서 이동하는 거리가 다른노드를 거치는 것보다 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijstra(start)


#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
