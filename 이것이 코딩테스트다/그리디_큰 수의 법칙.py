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
n, m, k = map(int, input().split()) #배열 크기, 숫자가 더해지는 횟수, 연속해서 더해질 수 있는 최대 횟수

data = list(map(int, input().split())) #크기가 n인 배열

data.sort() #입력받은 수 정렬
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수

result = 0

while True:
    for i in range(k): #가장 큰 수를 k번 더하기
        if m == 0: 
            break #반복문(for문) 탈출
        result += first
        m -= 1
    if m == 0:
        break #반복문(while문) 탈출
    result =+ second
    m -= 1
    
print(result)

# +
#수열 특성 이용
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k #m/(k+1)은 수열이 반복되는 횟수, k를 곱해주면 가장 큰 수가 등장하는 횟수
count += m%(k+1) #나머지만큼 가장 큰 수가 추가로 ㅐㅎ

result = 0
result += (count) * first #가장 큰 수 더하기
result += (m-count) * second #두 번째로 큰 수 더하기

print(result)
