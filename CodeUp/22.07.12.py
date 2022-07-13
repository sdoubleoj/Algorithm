#!/usr/bin/env python
# coding: utf-8

# ### [6041] 정수 2개 입력받아 나눈 나머지 계산
# - 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력
# - 2개의 정수(a, b)가 공백으로 구분되어 입력

# In[ ]:


num1, num2 = map(int, input().split())

print(num1%num2)


# ### [6042] 실수 1개 입력받아 소숫점이하 자리 변환
# - 실수 1개를 입력받아 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력

# In[ ]:


num = float(input())
print( format(num, ".2f") )


# ### [6043] 실수 2개 입력받아 나눈 결과 계산
# - 실수 2개(f1, f2)를 입력받아 f1 을 f2 로 나눈 값을 출력. 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력
# - 2개의 실수(f1, f2)가 공백으로 구분되어 입력

# In[ ]:


f1, f2 = map(float, input().split())
print( format(f1/f2,".3f") )


# ### [6044] 정수 2개 입력받아 자동 계산
# - 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산. (단, b는 0이 아님)
# - 정수 2개가 공백을 두고 입력

# In[ ]:


n1,n2 = map(int, input().split())

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1//n2)
print(n1%n2)
print( format(n1/n2,".2f") )


# ### [6045] 정수 3개 입력받아 합과 평균 출력
# - 정수 3개를 입력받아 합과 평균을 출력
# - 정수 3개가 공백을 두고 입력
# - 합과 평균을 공백을 두고 출력, 평균은 소숫점 이하 셋째 자리에서 반올림하여 둘째 자리까지 출력

# In[ ]:


n1,n2,n3 = map(int, input().split())
total = n1+n2+n3
print(total, format(total/3,".2f") )


# <br>
# 
# ### [6046] (Bit-Shift Operator) 정수 1개 입력받아 2배 곱해 출력
# - 정수 1개를 입력받아 2배 곱해 출력
# - **Bit-Shift Operator**
#     - 정수를 2배로 곱하거나 나누어 계산
#     - 왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,가장 오른쪽에 있는 1비트는 사라짐.
#     - python에서 실수 값에 대한 비트시프트 연산은 허용되지 않고 오류 발생

# In[ ]:


num = int(input())
print(num<<1)


# ### [6047] 2의 거듭제곱 배로 곱해 출력
# - 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력 (0 <= a <= 10, 0 <= b <= 10)

# In[ ]:


a,b = map(int, input().split())
print(a<<b)


# ### [6048] 정수 2개 입력받아 비교-1
# - 두 정수(a, b)를 입력받아
# a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램

# In[ ]:


a, b = map(int, input().split())
print(a<b)


# ### [6049] 정수 2개 입력받아 비교-2
# - 두 정수(a, b)를 입력받아
# a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램

# In[ ]:


a,b = map(int, input().split())

print(a==b)


# ### [6050] 정수 2개 입력받아 비교-3
# - 두 정수(a, b)를 입력받아
# b의 값이 a의 값 보다 크거나 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램

# In[ ]:


a,b = map(int, input().split())

print(a<=b)


# ### [6051] 정수 2개 입력받아 비교-4
# - 두 정수(a, b)를 입력받아
# a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력하는 프로그램

# In[ ]:


a,b = map(int, input().split())

if a != b:
    print(True)
elif a == b:
    print(False)

