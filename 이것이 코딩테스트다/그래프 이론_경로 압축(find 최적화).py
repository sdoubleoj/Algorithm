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
# 경로 압축을 통해 find 연산 최적화 - 루트 노드에 더욱 빠르게 접근하여 시간 복잡도 개선
def find_parent(parent, x):
    if parent[x] != x: #루트 노드가 아니라면,
         parent[x] = find_parent(parent, parent[x]) #해당 노드의 루트 노트가 바로 부모 노드가 됨
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
for i in range(1, v+1):
    parent[i] = i


for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')


print()


print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
