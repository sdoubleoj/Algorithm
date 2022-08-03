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

#1
#ANIMAL_INS 테이블, 동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;

#2
#동물 보호소에 들어온 모든 동물의 이름과 보호 시작일 조회, 이때 결과는 ANIMAL_ID 역순
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;

#3
#동물 보호소에 들어온 동물 중 아픈 동물('Sick')의 아이디와 이름 조회, 이때 결과는 아이디 순
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID ASC;

#4
#동물 보호소에 들어온 동물 중 젊은 동물(not 'Aged')의 아이디와 이름을 조회, 이때 결과는 아이디 순
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID ASC;

#5
#동물 보호소에 들어온 모든 동물의 아이디와 이름을 ANIMAL_ID순으로 조회
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;

#6
#모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 조회
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC;

# +
#7
#동물 보호소에 가장 먼저 들어온 동물의 이름 조회
SELECT NAME
FROM ANIMAL_INS
WHERE DATETIME = (SELECT MIN(DATETIME)
                 FROM ANIMAL_INS);

# SELECT NAME 
# FROM ANIMAL_INS
# ORDER BY DATETIME
# LIMIT 1;
