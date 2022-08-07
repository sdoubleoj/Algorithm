/*
1)
동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회
단, ID는 오름차순 정렬
*/
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME is null
ORDER BY ANIMAL_ID ASC;

/*
2
동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회
단, ID는 오름차순 정렬
*/
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME is not null
ORDER BY ANIMAL_ID ASC;


/* 3)
동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회
이름이 없는 동물의 이름은 "No name"으로 표시
*/

SELECT ANIMAL_TYPE, IFNULL(NAME,'No name'), SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;

/* SELECT ANIMAL_TYPE, 
        CASE WHEN NAME is null THEN 'No name' 
        ELSE NAME
        END AS NAME
        , SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC; */