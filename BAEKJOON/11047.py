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
n, k = map(int, input().split()) #동전 종류, 가치 합

coins = [] #동전 종류
result = 0 #필요한 동전 개수 최솟값
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

for coin in coins:
    result += (k//coin)
    k %= coin

print(result)
