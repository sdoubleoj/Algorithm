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

# [6052][논리연산] 정수 입력받아 참 거짓 평가
# - 정수가 입력되었을 때, True/False 로 평가해주는 프로그램
# - 정수값 0은 False, 나머지 정수 값들은 True
# - 빈 문자열 "" 나 ''는 False, 나머지 문자열들은 True

# +
n = int(input())

print(bool(n))
# -

# [6053][논리연산] 참 거짓 바꾸기 (NOT연산)
# - 정수값이 입력될 때,그 불 값을 반대로 출력하는 프로그램

num = bool(int(input()))
print(not num)

# [6054][논리연산] 둘 다 참일 경우만 참 출력 (AND연산)

# +
#1
n1, n2 = map(int, input().split())
print( (n1==True) & (n2==True) 

#2
n1, n2 = input().split()
print( bool(int(n1)) & bool(int(n2)) )
# -

# [6055][논리연산] 하나라도 참이면 참 출력 (OR연산)

n1, n2 = input().split()
print( bool(int(n1)) or bool(int(n2)) )

# [6056][논리연산] 참/거짓이 서로 다를 때에만 참 출력

# +
n1, n2 = map(int, input().split())
n1 = bool(n1)
n2 = bool(n2)

print( (n1 & (not n2)) | ((not n1) & n2) )
# -

# [6057][논리연산] 참/거짓이 서로 같을 때에만 참 출력

n1, n2 = map(int, input().split())
print( bool(n1) == bool(n2) )

# [6058][논리연산] 둘 다 거짓일 경우만 참 출력

n1, n2 = map(int, input().split())
print( (bool(n1) == False) & (bool(n2) == False)

# [6059][비트단위논리연산] 비트단위로 NOT 하여 출력
# - 비트단위(bitwise) 연산자  
#     ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
#     <<(bitwise left shift), >>(bitwise right shift)
# - 참고  
#     컴퓨터에 저장되는 모든 데이터들은 2진수 형태로 바뀌어 저장됨. 0과 1로만 구성되는 비트단위들로 변환되어 저장되는데, 양의 정수는 2진수 형태로 바뀌어 저장되고, 음의 정수는 "2의 보수 표현"방법으로 저장됨.  
#     ~n = -n-1  
#     -n = ~n+1

n = int(input())
print( ~n )

# [6060][비트단위논리연산] 비트단위로 AND 하여 출력
# - 비트단위 and 연산  
#     : 두 비트열이 주어졌을 때, 둘 다 1인 부분의 자리만 1로  
#     3 : 00000000 00000000 00000000 00000011  
#     5 : 00000000 00000000 00000000 00000101  
#     3 & 5 : 00000000 00000000 00000000 00000001
# - 네트워크에 연결되어 있는 두 개의 컴퓨터가 데이터를 주고받기 위해 같은 네트워크에 있는지 아닌지를 판단하는데 사용됨
# - 빠른 계산이 필요한 그래픽처리에서 마스크연산(특정 부분을 가리고 출력하는)을 수행하는 데에도 효과적으로 사용됨

n1, n2 = map(int, input().split())
print(n1&n2)

# [6061][비트단위논리연산] 비트단위로 OR 하여 출력
# - 비트단위 or 연산  
#     : 둘 중 하나라도 1인 자리를 1로

n1, n2 = map(int, input().split())
print(n1|n2)

# [6062][비트단위논리연산] 비트단위로 XOR 하여 출력
# - 비트단위(bitwise) 연산자 ^(xor, circumflex/caret, 서컴플렉스/카릿)를 사용
# - ^은 수학식에서 거듭제곱(power)을 나타내는 기호와 모양은 같지만,  
# C언어에서는 전혀 다른 배타적 논리합(xor, 서로 다를 때 1)의 의미를 가짐
# - 그래픽 처리에서  
# 두 장의 이미지가 겹쳐졌을 때 색이 서로 다른 부분만 처리할 수 있음.  
# 배경이 되는 그림과 배경 위에서 움직이는 그림이 있을 때,  
# 두 그림에서 차이만 골라내 배경 위에서 움직이는 그림의 색으로 바꿔주면  
# 전체 그림을 구성하는 모든 점들의 색을 다시 계산해 입히지 않고  
# 보다 효과적으로 그림을 처리할 수 있게 됨

n1, n2 = map(int, input().split())
print(n1^n2)

# [6063][3항연산] 정수 2개 입력받아 큰 값 출력
# - 3항연산  
#     "x if C(conditional expression) else y"

n1, n2 = map(int, input().split())
print (n1 if (n1>=n2) else n2)

# [6064][3항연산] 정수 3개 입력받아 가장 작은 값 출력

# +
n1, n2, n3 = map(int, input().split())

#print((n1 if n1<n2 else n2) if ((n1 if n1<n2 else n2)<n3) else n3)

min1 = (n1 if n1<n2 else n2)
min2 = (min1 if min1<n3 else n3)

print(min2)
# -

# [6065][조건/선택실행구조] 정수 3개 입력받아 짝수만 출력

# +
n1, n2, n3 = map(int, input().split())

if (n1%2 == 0):
    print(n1)
    
if (n2%2 == 0):
    print(n2)
    
if (n3%2 == 0):
    print(n3)
# -

# [6066][조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력

# +
n1, n2, n3 = map(int, input().split())

if (n1%2 == 0):
    print("even")
else:
    print("odd")
    
if (n2%2 == 0):
    print("even")
else:
    print("odd")
    
if (n3%2 == 0):
    print("even")
else:
    print("odd")
# -

# [6067][조건/선택실행구조] 정수 1개 입력받아 분류
# 음수이면서 짝수이면, A  
# 음수이면서 홀수이면, B  
# 양수이면서 짝수이면, C  
# 양수이면서 홀수이면, D  

# +
n1 = int(input())

if n1 < 0:
    if n1%2==0:
        print("A")
    else:
        print("B")
else:
    if n1%2==0:
        print("C")
    else:
        print("D")
# -

# [6068][조건/선택실행구조] 점수 입력받아 평가 출력  
# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력  
# 평가 기준  
# 90 ~ 100 : A  
# 70 ~   89 : B  
# 40 ~   69 : C  
# 0 ~   39 : D  

# +
score = int(input())

if score>=90:
    print("A")
elif score>=70:
    print("B")
elif score>=40:
    print("C")
else:
    print("D")
# -

# [6069][조건/선택실행구조] 평가 입력받아 다르게 출력  
# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력  
#     A : best!!!  
#     B : good!!  
#     C : run!  
#     D : slowly~  
#     나머지 문자들 : what?

# +
grade = input()

if grade=='A':
    print('best!!!')
elif grade=='B':
    print('good!!')
elif grade=='C':
    print('run!')
elif grade=='D':
    print('slowly~')
else:
    print('what?')
# -

# [6070][조건/선택실행구조] 월 입력받아 계절 출력  
# 12, 1, 2 : winter  
#   3, 4, 5 : spring  
#   6, 7, 8 : summer  
#   9, 10, 11 : fall  

# +
month = int(input())

if month//3==1:
    print('spring')
elif month//3==2:
    print('summer')
elif month//3==3:
    print('fall')
else:
    print('winter')
