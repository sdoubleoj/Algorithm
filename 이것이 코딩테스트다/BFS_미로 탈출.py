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

# 입력 조건
# - 첫째 줄에 두 정수 N,M(4<=N,M<=200) 주어짐
# - 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보 주어짐
# - 각각의 수들은 공백없이 붙어서 입력으로 제시
# - 시작 칸과 마지막 칸은 항상 1  
#
# 출력 조건
# - 첫째 줄에 최소 이동 칸의 개수 출력

# +
from collections import deque

n,m = map(int, input().split())

graph = [] #맵 정보
for i in range(n):
    graph.append(list(map(int,input())))
    
#이동방향 정의
#상하좌우 : (-1,0),(+1,0),(0,-1),(0,+1)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    queue = deque() #큐 구현
    queue.append((x,y))
    
    while queue: #큐가 빌 때까지(False) 반복
        x, y = queue.popleft() #먼저 들어온 노드 꺼내기
        
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #미로찾기 공간 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m: 
                continue
            #괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1: #새로 방문하는 노드는 (이전 노드의 거리+1)값을 가지므로 처음 방문하는 노드는 1을 가짐
                graph[nx][ny] = graph[x][y] +1 #이전 노드의 거리+1 (방문처리)
                queue.append((nx,ny)) #큐에 인접 노드 삽입
    
    #가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1] #counted from idx 0 ~
            
#BFS를 수행한 결과 출력
print(bfs(0,0))
