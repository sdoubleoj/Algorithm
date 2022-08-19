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
INF = int(1e9)

# 노드 및 간선 개수
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현) 생성, 모든 값을 무한으로 초기화
graph = [ [INF] * (n+1) for _ in range(n+1) ] # (n+1)*(n+1) 표

# 자기 자신으로 가는 바용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        # 도달할 있는 경우 거리 출력
        else:
            print(graph[a][b], end=' ')
    print()
            
