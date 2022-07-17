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

# [6071][반복실행구조] 0 입력될 때까지 무한 출력  
# 임의의 정수가 줄을 바꿔 계속 입력된다.  
# -2147483648 ~ +2147483647, 단 개수는 알 수 없다.  
#   
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단

while True:
    n = int(input())
    if n != 0:
        print(n)
    else:
        break

# [6072][반복실행구조] 정수 1개 입력받아 카운트다운 출력    
# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력

# +
#1
while True:
    n = int(input())
    for i in range(n,0,-1): #reversed(range(1,n+1))
        print(i)
       
#2
a = int(input())
while a!=0:
    print(a)
    a-=1
# -

# [6073][반복실행구조] 정수 1개 입력받아 카운트다운 출력  
# 1만큼씩 줄이면서 카운트다운 수가 0이 될 때까지 한 줄에 1개씩 출력  
# 입력:5, 출력:4,3,2,1,0

# +
#1
n = int(input())
while n>0:
    print(n-1)
    n-=1
    
#2
a=int(input())

while a!=0:
    a=a-1
    print(a)
# -

# [6074][반복실행구조] 문자 1개 입력받아 알파벳 출력  
# 영문 소문자(a ~ z) 1개가 입력되었을 때,  
# a부터 그 문자까지의 알파벳을 순서대로 출력

# +
#1
a = ord("a")
c = ord(input())
if c != a:
    for i in range(a,c+1):
        print(chr(i),end=' ')
else:
    print("a")

#예시
c=input()
i = ord('a')
c = ord(c)

while i<=c:
    print(chr(i), end=' ')
    i+=1
# -

# [6075][반복실행구조] 정수 1개 입력받아 그 수까지 출력  
# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력

# +
n = int(input())
for i in range(n+1): #range(start,end,step)
    print(i)
    
#예시
n=int(input())
i=0
while i<=n:
    print(i)
    i+=1
# -

# [6077][종합] 짝수 합  
# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합

n = int(input())
even_sum = 0
for num in range(n+1): #range(1,n+1)
    if num%2==0:
        even_sum += num
print(even_sum)

# [6078][종합] 원하는 문자가 입력될 때까지 반복 출력  
# 영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램

while True:
    s = input()
    print(s)
    if s=='q':
        break 

# [6079][종합] 언제까지 더해야 할까?  
# 1, 2, 3 ... 을 계속 더해 나갈 때, 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만 계속 더하는 프로그램
# - 1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가, 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력

# +
#1
n_sum = 0
add_num = 0 
n = int(input())

while True: #1부터 정수를 계속 더해나가다가
    n_sum += (add_num+1)
    add_num += 1
    if n_sum >= n: #정수합이 입력값보다 같거나 커지면(조건불만족)
        break
print(add_num) #조건 만족한 경우의 마지막 정수

#best
n_sum = 0
add_num = 0 
n = int(input())

while n_sum<n:
    add_num += 1
    n_sum += add_num
    
print(add_num)
# -

# [6080][종합] 주사위 2개 던지기  
# 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,  
# 나올 수 있는 모든 경우를 출력  
# - 입력: 서로 다른 주사위 2개의 면의 개수 n, m이 공백을 두고 입력(단, n, m은 10이하의 자연수)
# - 출력: 나올 수 있는 주사위의 숫자를 한 세트씩 줄을 바꿔 모두 출력.
# 첫 번째 수는 n, 두 번째 수는 m으로 고정해 1부터 오름차순 순서로 출력.

# +
n,m = map(int,input().split())

dice_1 = list(range(1,n+1))
dice_2 = list(range(1,m+1))

for n1 in dice_1:
    for n2 in dice_2:
        print(n1,n2)
