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
# 특정 원소 x가 속한 집합 찾기(union 연산 이후 사용되는 함수)
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합 합치기 - '루트' 노드가 같은 원소끼리 동일 집합
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    #번호가 더 작은 원소가 부모 노드가 되도록 구현
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

        
# 초기 단계
# 노드(원소) 개수 V & 간선(union 연산) 개수 e
v, e = map(int, input().split())
parent = [0] * (v+1) #부모 테이블 초기화
# 부모 테이블 상에서, 모든 원소(인덱스)의 부모 노드를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산(간선) 실행
for i in range(e):
    a, b = map(int, input().split()) #union 연산 정보 입력
    union_parent(parent, a, b)
    
# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
    
print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
