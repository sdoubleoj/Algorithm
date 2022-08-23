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

edges = [] #모든 간선을 담을 리스트
result = 0 #최소 신장 트리를 만드는 최종 비용

for i in range(1, v+1):
    parent[i] = i

for _ in range(1, v+1):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) #비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정

# 간선을 비용순으로 정렬
edges.sort()


for edge in edges: #간선을 하나씩 확인하며
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

        
print(cost)
