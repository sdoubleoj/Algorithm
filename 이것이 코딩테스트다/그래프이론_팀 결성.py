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
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

n, m = map(int, input().split())
parent = [0] * (n+1) #부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i


# 각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())
    
    if oper == 0: # 팀 합치기(union)일 경우,
        union_parent(parent, a, b)
    elif oper == 1: #같은 팀 확인 여부(find)일 경우,
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
