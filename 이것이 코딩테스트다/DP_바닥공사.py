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

# $ a_i = a_{i-1} + a_{i-2}*2 $  
# - $ i-2 $ 까지 길이가 덮개로 이미 채워져 있는 경우, 덮개 채우는 방법은 2가지 존재

# +
n = int(input()) #1 <= n <= 1,000

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3,n+1): #from 3 to n
    d[i] = ( d[i-1] + d[i-2]*2 )%796796 #just 결괏값이 굉장히 커질 수 있기 때문
    
print(d[n])
