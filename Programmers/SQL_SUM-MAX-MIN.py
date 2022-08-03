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
#1
#가장 최근에 들어온 동물은 언제 들어왔는지 조회

SELECT MAX(DATETIME)
FROM ANIMAL_INS;

# SELECT DATETIME
# FROM ANIMAL_INS
# WHERE DATETIME = (SELECT MAX(DATETIME)
#                  FROM ANIMAL_INS);

# SELECT DATETIME
# FROM ANIMAL_INS
# ORDER BY DATETIME DESC
# LIMIT 1;

# +
#2
#동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회

SELECT MIN(DATETIME)
FROM ANIMAL_INS;

# SELECT DATETIME
# FROM ANIMAL_INS
# ORDER BY DATETIME
# LIMIT 1;
# -

#3
#동물 보호소에 동물이 몇 마리 들어왔는지 조회
SELECT COUNT(*)
FROM ANIMAL_INS;

#4
#동물 보호소에 들어온 동물의 이름은 몇 개인지 조회. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS;
