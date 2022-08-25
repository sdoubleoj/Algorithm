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
# min() 이용

n, m = map(int, input().split())

result = 0

# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수 찾기
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data) #현재 줄에서 '가장 작은 수' 찾기'
    result = max(result, min_value) #'가장 작은 수'들 중에서 가장 큰 수 찾기'
    
print(result)

# +
# 2중 반복문 구조 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    
    #현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    #'가장 작은 수'들 중에서 가장 큰 수 찾기'
    result = max(result, min_value)

print(result)
