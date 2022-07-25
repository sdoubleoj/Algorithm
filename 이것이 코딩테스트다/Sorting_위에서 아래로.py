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
n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))
    
#기본 정렬 라이브러리 이용 내림차순 정렬
array = sorted(array,reverse=True)

for i in array:
    print(i,end=' ')
