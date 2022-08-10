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

# - $ a_{i-k} $를 만드는 방법이 존재하는 경우: $ a_i = min( a_i, a_{i-k}+1 ) $
# - ~ 존재하지 않는 경우: $ a_i = 10,001 $  (max(m)==10,000)

# +
#n: 화폐 가짓수, m: 화폐 가치의 합
# 1 <= n <= 100, 1 <= m <= 10,000
n, m = map(int, input().split()) # ex) 2 15

#n개의 화폐 단위 정보 
array = []
for i in range(n): #ex) 2
     array.append(int(input())) #ex) [2,3]

# 각 인덱스(금액)을 만들 수 있는 화폐구성이 존재하지 않는 경우인 10,001로 DP 테이블 초기화
d = [10001] * (m+1) #d[0] ~ d[15], d[i] = 10001

d[0] = 0 #화폐를 하나도 사용하지 않았을 때
for i in range(n): #n개의 모든 화폐 단위에 대해 차례대로 점화식 적용 
    for j in range(array[i], m+1): #각 인덱스의 값, 즉 화폐 사용 개수의 최솟값은 더 작은 값으로 갱신
        if d[j-array[i]] != 10001: #금액(j-arrya[i])를 만들 수 있는 최소한의 화폐 개수
            d[j] = min(d[j], d[j-array[i]]+1)
            
if d[m] == 10001: #최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
