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

# [6081]16진수 구구단 출력  
# - 16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)
# - A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력 (단, A ~ F 까지만 입력)
# - 출력 예시: B*1=B

# +
c = int(input(),16)

for i in range(1,16):
    print('%X*%X=%X' %(c,i,c*i))

#hex(),%x,%X : 정수를 16진수 문자열로 변환
#print(-,sep='') : 공백없이 모두 붙여 출력
# -

# [6082] 3 6 9 게임  
# - 30 보다 작은 정수 1개 입력(1 ~ 29)
# - 1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데,  
# 3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력
# - 출력 예시 : 1 2 X 4 5 X 7 8 X

# +
n = input()

for i in range(1,int(n)+1):
    i = str(i)
    if ('3'in i)or('6'in i)or('9'in i):
        print('X',end=' ')
    else:
        print(i,end=' ')

# +
n = int(input())

for i in range(1, n+1):
    if i%10==3 or i%10==6 or i%10==9 :
        print("X", end=' ')
    else :
        print(i, end=' ')
# -

# [6083] 빛 섞어 색 만들기
# - 빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,  
# 주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산
# - 입력:  
#     빨녹파(r, g, b) 각 빛의 가짓수가 공백을 두고 입력  
#     예를 들어, 3 3 3 은 빨녹파 빛에 대해서 각각 0~2까지 3가지 색이 있음을 의미(0 <= r,g,b <= 127)
# - 출력:  
# 만들 수 있는 rgb 색의 정보를 오름차순(계단을 올라가는 순, 12345... abcde..., 가나다라마...)으로 줄을 바꿔 모두 출력하고, 마지막에 그 개수를 출력

# +
from itertools import product

r,g,b = map(int,input().split())
r = list(str(x) for x in range(r))
g = list(str(x) for x in range(g))
b = list(str(x) for x in range(b))

rgb_list = [r,g,b]
rgb_prd = list(product(*rgb_list))

for x in rgb_prd:
    print(' '.join(x))

print(r*g*b)

# +
r,g,b = map(int,input().split())

for x in range(r):
    for y in range(g):
        for z in range(b):
            print(x,y,z)
    
print(r*g*b)
# -

# [6084] 소리 파일 저장용량 계산  
#
# 1초 동안 마이크로 소리강약을 체크하는 횟수를 h (Hz:1초에 몇 번 체크하는가)  
#
# 한 번 체크한 값을 저장할 때 사용하는 비트수를 b (2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)  
#
# 좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c (모노는 1개, 스테레오는 2개의 트랙으로 저장 의미)  
#
# 녹음할 시간(초) s가 주어질 때,  
#
# 필요한 저장용량(MB)을 계산하는 프로그램
#
# - 입력:  
# h, b, c, s 가 공백을 두고 입력  
# h는 48,000이하, b는 32이하(단, 8의배수), c는 5이하, s는 6,000이하의 자연수
#
# - 출력:  
# 필요한 저장 공간을 MB 단위로 바꾸어 출력  
# 단, 소수점 첫째 자리까지의 정확도로 출력하고 MB를 공백을 두고 출력

h,b,c,s = map(int, input().split())
print(round(h*b*c/8/1024/1024*s,1),'MB')

# [6084] 그림 파일 저장용량 계산  
#
# 그림을 구성하는 한 점(pixel, 픽셀)의 색상을 빨강(r), 초록(g), 파랑(b)의 3가지의 빛의 세기 값으로 따로 변환하여 저장  
#
# r, g, b 각 색에 대해서 8비트(0~255, 256가지 가능)씩을 사용한다고 하면, 한 점의 색상은 3가지 r, g, b의 8비트+8비트+8비트로 총 24비트로 표현해 총 2^24 가지의 서로 다른 빛의 색깔을 사용할 수 있는 것  
#
# w*h 사이즈의 이미지의 각 점에 대해 24비트로 저장하면 그 이미지를 저장하기 위한
# 저장 용량을 계산할 수 있음  
#
# 위와 같이 이미지의 원래(raw) 데이터를 압축하지 않고 그대로 저장하는 대표적인 이미지 파일이 *.bmp 파일이며, 비트로 그림을 구성한다고 하여 '비트맵 방식' 또는 '래스터 방식'이라고 함
#
# - 이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때, 압축하지 않고 저장하기 위해 필요한 저장 용량 계산 프로그램

w,h,b = map(int, input().split())
#print(round(w*h*b/8/1024/1024,2),'MB')
print('%.2f MB' %(round(w*h*b/8/1024/1024,2)))
