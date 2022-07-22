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

# [6096][List] 바둑알 십자 뒤집기  
# - 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
# n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램  
# - 십자 뒤집기  
#     : 그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 
# 다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것  
# 어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀜
# - 입력:  
#     바둑알이 깔려 있는 상황 - 19 * 19 크기의 정수값으로 입력  
#     십자 뒤집기 횟수(n)  
#     십자 뒤집기 좌표가 횟수(n) 만큼 입력 (단, n은 10이하의 자연수)

#바둑알 상황 (한 행씩 입력)
b = [list(map(int, input().split())) for _ in range(19)]

# +
#십자 뒤집기 횟수
n = int(input())

#좌표
for _ in range(n):
    x,y = map(int,input().split())
    
    for j in range(19):
        #해당 좌표의 모든 가로줄 색 바꾸기(열 고정)
        if b[j][y-1]==1:
            b[j][y-1] = 0
        else:
            b[j][y-1] = 1
        
        #세로줄 색 바꾸기(행 고정)
        if b[x-1][j]==1:
            b[x-1][j] = 0
        else:
            b[x-1][j] = 1
    
for i in range(19):
    for j in range(19):
        print(b[i][j], end=' ')
    print()

# +
#십자 뒤집기 횟수
n = int(input())

#좌표
for _ in range(n):
    x,y = map(int,input().split())
    
    for j in range(1,20): #좌표 (1,1)부터 시작
        #해당 좌표의 모든 가로줄 색 바꾸기(열 고정)
        if b[j][y]==1:
            b[j][y] = 0
        else:
            b[j][y] = 1
        
        #세로줄 색 바꾸기(행 고정)
        if b[x][j]==1:
            b[x][j] = 0
        else:
            b[x][j] = 1
    
for i in range(1,20):
    for j in range(1,20):
        print(b[i][j], end=' ')
    print('')
# -

# [6097][List] 설탕과자 뽑기  
# - 길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임
# - 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l), 막대를 놓는 방향(d:가로는 0, 세로는 1)과 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,격자판을 채운 막대의 모양을 출력하는 프로그램  
#
# - 입력:  
#     첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력  
#     두 번째 줄에 놓을 수 있는 막대의 개수(n)  
#     세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)  
#     (1 <= w, h <= 100, 1 <= n <= 10, d = 0 or 1, 1 <= x <= 100-h, 1 <= y <= 100-w)
#     
# - 출력:  
#     모든 막대를 놓은 격자판의 상태를 출력  
#     막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력  
#     단, 각 숫자는 공백으로 구분하여 출력

# +
h, w = map(int, input().split())
n = int(input()) #막대 개수

info = []
for _ in range(n): #n개 막대의 정보 입력
    info.append(list(map(int, input().split())))
    
#격자판 - 2차원 리스트
b = [ [0]*w for _ in range(h)]

# 막대1 - 길이 2, 가로 방향0, (1,1)에서 시작
# 막대2 - 길이 3, 세로1, (2,3)
# 막대3 - 길이 4, 세로1, (2,5)

for j in range(n):
    i = info[j][0]
    d = info[j][1]
    x = info[j][2]-1
    y = info[j][3]-1
    
    if d == 0:
        for _ in range(i):
            b[x][y] = 1
            y += 1
    else:
        for _ in range(i):
            b[x][y] = 1
            x += 1
    
for i in range(h):
    for j in range(w):
        print(b[i][j], end=' ')
    print('')
# -

# [6098][List] 성실한 개미  
#
# - 개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직임 (오른쪽에 길이 나타나면 다시 오른쪽으로 움직임)  
#     먹이를 찾았거나, 더 이상 움직일 수 없을 때까지 오른쪽 or 아래쪽으로만 움직임  
#     
# - 미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,먹이가 2로 주어질 때, 개미의 이동경로 예상  
#     단, 맨 아래의 가장 오른쪽에 도착한 경우 or 더 이상 움직일 수 없는 경우, 더이상 이동하지 않고 그 곳에 머무른다고 가정  
#     
# - 미로 상자의 테두리는 모두 벽으로 되어 있으며, 개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발
#
# - 입력:  
#     10*10 크기의 미로 상자 구조 & 먹이 위치 입력
# - 출력:  
#     개미가 이동한 경로를 9로 표시해 출력

box = [ list(map(int,input().split())) for _ in range(10) ]

box

# +


#현재 좌표
x, y = 1, 1  
    
while True:
    
    #갈 수 있는 곳
    if box[x][y] == 0:
        box[x][y] = 9
    #먹이 발견
    elif box[x][y] == 2:
        box[x][y] = 9
        break
        
    #더 이상 이동 불가 or 맨 아래의 가장 오른쪽에 도착
    if (box[x+1][y] == 1 and box[x][y+1]==1) or (x == 9 and y == 9):
        break
        
    #오른쪽에 벽이 나타난 경우 아래로 이동
    if box[x][y+1] == 1:
        x += 1
    #아래에 벽이 나타난 경우 오른쪽으로 이동
    elif box[x+1][y] == 1:
        y += 1
        
        
for i in range(10):
    for j in range(10):
        print(box[i][j], end=' ')
    print()
# -

m = box

# +
# ex - s

x = 1
y = 1
while True :
    if m[x][y] == 0 :
        m[x][y] = 9
    elif m[x][y] == 2 :
        m[x][y] = 9
        break

    if (m[x][y+1]==1 and m[x+1][y]==1) or (x==8 and y==8) :
        break

    if m[x][y+1] != 1 :
        y += 1
    elif m[x+1][y] != 1 :
        x += 1
    

for i in range(10) :
    for j in range(10) :
        print(m[i][j], end=' ')
    print()

# -


