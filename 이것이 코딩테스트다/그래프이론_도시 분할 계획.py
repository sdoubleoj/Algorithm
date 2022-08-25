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
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

        
v, e = map(int, input().split())
parent = [0] * (v+1)

edges = [] #모든 간선 담을 리스트
result = 0 #최종 비용

#모든 간선 정보
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) #비용순 정렬을 위해 cost를 첫 번쨰 원소로 설정

edges.sort() #비용순으로 간선 정렬
last = 0 #최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선


for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    # 동일 부모를 가지면 사이클이 발생할 수 있기 때문
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost


#이미 edges는 비용순으로 정렬되어 있기 때문에, 가장 마지막의 cost가 최소 신장 트리를 구성하는 간선 중 최대비용의 간선임
print(result - cost) 
