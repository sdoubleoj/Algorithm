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

배열A,B
각각 N개의 원소
최대 K번의 바꿔치기
배열A의 합이 최댓값
.. A의 최소원소 <-> B의 최대원소

# +
n, k  = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True) #reverse()는 내림차순 정렬이 아니라 인덱스를 뒤집는 것임!!

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
        
print(sum(a))
# -


