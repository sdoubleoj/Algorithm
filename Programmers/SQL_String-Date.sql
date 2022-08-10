/* 1
동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 아이디 순으로 조회 */
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID


/* 2
동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 '개'의 아이디와 이름을 이름 순으로 조회
단, 이름의 대소문자 구분하지 않음 */
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' and NAME LIKE '%el%' 
ORDER BY NAME


/* 3
동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회
이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시 */
SELECT ANIMAL_ID, NAME, 
    CASE 
        WHEN SEX_UPON_INTAKE LIKE '%intact%'
        THEN 'X'
        ELSE 'O'
    END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID


/* 4
입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회
이때 결과는 보호 기간이 긴 순으로 조회 */
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I INNER JOIN ANIMAL_OUTS O --LEFT,RIGHT,INNER 상관X
        ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY O.DATETIME-I.DATETIME DESC
LIMIT 2


/* 5
ANIMAL_INS 테이블에 등록된 모든 레코드에 대해, 
각 동물의 아이디와 이름, 들어온 날짜를 아이디 순으로 조회 */
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, "%Y-%m-%d") 날짜 --y,m,d 대소문자에 따라 포맷 달라짐
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
