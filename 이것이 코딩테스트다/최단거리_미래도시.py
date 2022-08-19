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
#플로이드 워셜 알고리즘

INF = int(1e9)
# 회사(노드) 개수 n, 경로(간선) 개수 m
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현) 및 무한 초기화
graph = [ [INF] * (n+1) for _ in range(n+1) ]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1
    a, b = map(int, input().split())
    graph[a][b] = 1

# 거쳐 갈 노드 K, 최종 목적지 노드 X
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 실행
for k in range(1, n+1): #거쳐 갈 노드 K를 기준으로 실행
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
# 알고리즘 수행 결과
distance = graph[1][k] + graph[k][x]

#도달 할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
else:
    print(distance) # 1>X>K 최소 이동 시간
