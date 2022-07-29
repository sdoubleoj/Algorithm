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
#파라메트릭 서치

# N - 가지고 있는 떡 개수 (1<=N<=1,000,000)
# M - 손님이 필요한 떡 길이 (1<=M<=2,000,000,000)

n, m = list(map(int, input().split()))
array = list(map(int, input().split())) #떡 각각의 높이

start = 0
end = max(array) # 0 <= 절단기높이 <= 가장 긴 떡의 길이)

#이진탐색 반복문 구현
result = 0
while start <= end:
    total = 0 #떡 높이 총합
    mid = (start+end)//2 #절단기 높이
    
    for x in array:
        if x > mid: #떡이 절단기보다 높으면
            total += x-mid
            
    if total < m: #손님이 필요한 양보다 적으면
        end = mid-1 #더 많이 자르기(왼쪽 부분 탐색)
    else: #양이 충분할 경우 덜 자르기(오른쪽 부분 탐색)
        result = mid #최대한 덜 잘랐을 때가 정답이므로, 이 부분에서 현재 절단기 높이인 mid를 result에 기록
        start = mid+1 #모든 n개의 떡의 시작점이 같으므로 떡을 덜 자르기 위해서는 시작점을 mid+1 해줘야 함
        
print(result) 
