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

# $a_i = min(a_{i-1}, a_{i/2}, a_{i/3}, a_{i/5}) + 1$

# +
x = int(input()) #1 <= x <= 30,000

d = [0] * 30001 #연산횟수의 최솟값을 저장할 DP 테이블 초기화
#d[1] = 0

#i에 대한 계산결과를 DP 테이블에 저장
for  i in range(2, x+1): #bottom-up DP
    #현재 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    
    #현재의 수가 2|3|5로 나누어 떨어지는 경우
    if i&2 == 0:
        d[i] = min(d[i], d[i//2]+1)   
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)    
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)
    
print(d[x])
