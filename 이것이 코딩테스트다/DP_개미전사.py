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

# $ a_i = max( a_{i-1}, a_{i-2} + k_i ) $

# +
n = int(input()) #3 <= n =< 100
array = list(map(int, input().split())) #모든 식량 정보

d = [0] * 100 #DP 테이블 초기화

#Bottom-Up
d[0] = array[0] #첫번째 창고의 식량
d[1] = max(array[0], array[1]) #두번째 창고 식량
for i in range(2, n): #2 ~ n-1 ;according to the idx num
    #i번째 창고를 털지 여부 결정할 때 (i-1)과 (i-2)만 고려
    #d[i-1] 선택 : 인접한 현재(i번째) 식량창고 털지 않음
    #d[i-2] 선택 : 인접한 현재(i번째) 식량창고도 털 수 있음
    d[i] = max(d[i-1], d[i-2]+array[i]) 
    
#계산된 결과
print(d[n-1])
