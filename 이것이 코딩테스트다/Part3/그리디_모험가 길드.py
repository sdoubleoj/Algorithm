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
n = int(inut().split()) #모험가의 수
fears = list(map(int, input().split())) #n명의 각 모험가의 공포도 (n이하의 자연수) #2 3 1 2 2

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

fear.sort()

for fear in fears: #낮은 공포도부터 하나씩 확인
    count += 1 #현재 그룹에 해당 모험가 포함시키기
    
    #그룹 참여 조건: 현재까지 그룹에 참여한 모험가의 수가 공포도 이상
    if count >= i:
        result += 1 #총 그룹의 수 증가시키기
        count = 0 #현재 그룹에 포함된 모험가의 수 초기화

#모험가 그룹의 최대 개수
print(result)
