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
#N,M을 공백으로 구분하여 입력받기 (1<=N,M>=1000)
n,m = map(int, input().split())

#2차원 리스트인 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

    
#DFS로 특정한 노드를 방문한 뒤, 연결된 모든 노드들도 방문
def dfs(x,y): #행,열
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문처리
        graph[x][y] = 1
        #상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y) #상
        dfs(x, y-1) #좌
        dfs(x+1 , y) #하
        dfs(x, y+1) #우
        return True
    
    return False #현재 노드를 이미 방문한 경우


#모든 노드(위치)에 음료수 채우기
result = 0 #한 번에 만들 수 있는 아이스크림 개수
#출발위치가 지정되어 있지 않기 때문에 (0,0)~(n-1,m-1) 순서로 탐색(이전 예제와 달리 graph의 idx 0부터 사용)
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1
            

print(result)
# -


