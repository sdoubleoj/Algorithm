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

# [6086]거기까지! 이제 그만~  
#
# - 1, 2, 3 ... 을 순서대로 계속 더해 합을 만드는데,그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램  
# (1부터 n까지 정수를 하나씩 더해 합을 만드는데,  
# 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제)

# +
t = int(input())
sn = 0
n = 1

while True:
    sn += n
    n += 1
    if sn >= t:
        print(sn)
        break
        
#2
a=int(input())
s=0
c=0

while True:
    s=s+c
    c=c+1
    if s>=a:
        break
    
print(s)
# -

# [6087] 3의 배수는 통과  
#
# - 1부터 입력한 정수까지 1씩 증가시켜 출력, 단 3의 배수인 경우는 출력하지 않도록 하는 프로그램
#   
# - 제어문 안에서의 continue  
#     : 반복 블록 내의 나머지 부분을 실행하지 않고, 다음 뱐복 단계로 넘어감

# +
n = int(input())

for i in range(1,n+1):
    if i%3==0:
        continue #무시하고 다음 반복 단계(i+1)로 넘어감
    print(i,end=' ')

# -

# [6088] 수 나열 - 등차수열
# - 시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때
# n번째 수를 출력하는 프로그램 (등차수열의 n번째 값 출력)

# +
a, d, n = map(int, input().split())

count = 1 #1번째 숫자부터 시작

while True:
    a += d 
    count += 1

    if count==n:
        break
        
print(a)

# +
a, d, n = map(int, input().split())

for _ in range(2, n+1):
   a+=d

print(a)
# -

# [6089] 수 나열하기  - 등비수열  
# - 시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때
# n번째 수를 출력하는 프로그램

a, r, n = map(int, input().split())
count = 1
while True:
    a *= r
    count += 1
    if count == n:
        print(a)
        break

# +
a, r, n = map(int, input().split())

for _ in range(1, n) :
  a = a*r

print(a)
# -

# [6090] 수 나열  
# - 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,
# n번째 수를 출력하는 프로그램
#

a, m, d, n = map(int, input().split())
count = 1
while True:
    
    a = a*m + d
    count += 1
    
    if count == n:
        print(a)
        break

# +
a, m, d, n = map(int, input().split())

for _ in range(n-1):
    a = a*m + d
    
print(a)
# -

# [6091] 함께 문제 푸는 날  
# -  같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가 매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?

# +
a,b,c = map(int, input().split())
d = 1

# d%a!=0 and d%b!=0 and d%c!=0 를 만족하는 것이 최소공배수이므로
while d%a!=0 or d%b!=0 or d%c!=0:
    d += 1
    
print(d)
# -

# [6092] 이상한 출석부 부르기  1
# - 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력
# - 

# +
n = int(input())
called = list(map(int, input().split()))
count = ['0']*23

for i in called:
    count[i-1] = str(int(count[i-1])+1)
    
print(' '.join(count))

# +
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

d = [] #출석번호별 불린 횟수 카운트 리스트
for i in range(24) : #24 -> 23 번호 그대로 인덱스로 쓰기 위함
  d.append(0)

for i in range(n) : #번호 불릴 때마다 카운트 +1
  d[a[i]] += 1 #2중 리스트

for i in range(1, 24) :
  print(d[i], end=' ')
# -

# [6093] 이상한 출석번호 2  
#
# - 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력

n = int(input())
called = list(map(int,input().split())) #list와 map 차이
called.reverse()
#sort, reverse 함수는 원본 리스트를 변경해주지만 return None 함수이므로
#called = called.reverse() 해주면 변수 called는 Nonetype이 됨
for n in called:
    print(n,end=' ')

# +
n = int(input())
a = input().split()

for i in range(n) :
    a[i] = int(a[i])

for i in range(n-1, -1, -1):
    print(a[i], end=' ')
# -

# [6094] 이상한 출석번호 3  
# - 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호 출력

# +
n = input()
called = list(map(int,input().split()))

print(min(called))

# +
n = int(input())
a = input().split()

for i in range(n) :
    a[i] = int(a[i])

min = a[0]
for i in range(0, n) :
    if a[i] < min :
        min = a[i] #최솟값 갱신 반복

print(min)
# -

# [6095][List Comprehension] 바둑판에 흰돌 놓기  
# - 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때, n개의 흰 돌이 놓인 위치를 출력하는 프로그램  
#
# - 입력:  
#     바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력됨  
#     둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력됨  
#     n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지이며, 똑같은 좌표는 입력되지 않음
#     
# - 출력:  
#     흰 돌이 올려진 바둑판의 상황을 출력  
#     흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력

# +
n = int(input())

#좌표 담을 리스트
x = []
y = []
for _ in range(n):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)

#바둑판 생성 - 2차원 리스트 초기화 > List Comprehension 필수
board = [[0]*19 for _ in range(19)]
#board = [ [0]*19 ]*19
#boolean값은 True인데 board[1][1]=1 했을 때 결과가 다름
# 내부적으로 포함된 19개의 리스트가 모두 동일한 객체에 대한 19개의 레퍼런스로 인식되기 때문

#해당 좌표에 바둑알 놓기
for i in range(n):
    board[x[i]-1][y[i]-1] = 1


for i in range(19):
    for j in range(19):
        print(board[i][j],end=' ')
    print('')

# +
#2
d=[]
for i in range(20) :
    d.append([])
        for j in range(20) : 
            d[i].append(0)

n = int(input())
for i in range(n) :
    x, y = input().split()
    d[int(x)][int(y)] = 1

for i in range(1, 20) :
    for j in range(1, 20) : 
        print(d[i][j], end=' ')
    print()

# -

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

#바둑알 상황 
board = [list(map(int, input().split())) for _ in range(19)]

# +
#십자 뒤집기 횟수
n = int(input())

#좌표
x = []
y = []
for _ in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

#뒤집기
for i in range(n):
    if board[x[i]][y[i]]==1:
        board[x[i]] = 0
        board[y[i]] = 0
    else:
        board[x[i]] = 1
        board[y[i]] = 1

for i in range(19):
    for j in range(19):
        print(board[i][j],end=' ')
    print('')
# -

0 0 0 1 0 0 1
0 0 0 1 0 0 1 
0 0 0 1 0 0 1 
1 1 1 1 1 1 1 
0 0 0 1 0 0 1
0 0 0 1 0 0 1 
0 0 0 1 0 0 1

board

board[4]

y


