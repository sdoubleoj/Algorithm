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
#'최대한 많이 나누기'
n, k = map(int, input().split())
result = 0

#n이 k 이상이라면 k로 계속 나누기
while n >= k:
    #n이 k로 나누어 떨어지지 아낳는다면 n에서 1씩 빼기
    while n%k != 0:
        n -= 1
        result += 1
    
    n //= k
    result += 1
    
while n > 1:
    n -= 1
    result += 1
    
print(result)

# +
#n이 100억 이상의 큰 수가 되는 경우 가정
n, k  = map(int, input().split())

result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//k) * k
    result += (n-target)
    n = target
    #n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break
    #k로 나누기
    result += 1
    n //= k
    
#마지막으로 남은 수에 대해 1씩 빼기
result += (n-1)
print(result)
