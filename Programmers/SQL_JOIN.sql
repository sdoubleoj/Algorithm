/* 1)
입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회 */
SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID not in (SELECT ANIMAL_ID
                        FROM ANIMAL_INS)
ORDER BY ANIMAL_ID;

/* SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS AS O
WHERE NOT EXISTS (
    SELECT I.ANIMAL_ID
    FROM ANIMAL_INS AS I
    WHERE O.ANIMAL_ID = I.ANIMAL_ID) */

/* SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O LEFT JOIN ANIMAL_INS I 
    ON (O.ANIMAL_ID = I.ANIMAL_ID)
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID */


/* 2
보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회, 이때 결과는 보호 시작일이 빠른 순으로 */
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I, ANIMAL_OUTS O
WHERE I.ANIMAL_ID = O.ANIMAL_ID and I.DATETIME > O.DATETIME
ORDER BY I.DATETIME;


/* 3
아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 보호시작일 순으로 조회
 */
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I LEFT JOIN ANIMAL_OUTS O
    ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID is null
ORDER BY I.DATETIME
LIMIT 3

/* SELECT NAME, DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID not in (SELECT ANIMAL_ID
                       FROM ANIMAL_OUTS)
ORDER BY DATETIME
LIMIT 3 */


/* 4
보호소에서 중성화 수술을 거친 동물 정보
보호소에 들어올 당시에는 중성화 되지 않았지만('Intact'), 보호소를 나갈 당시에는 중성화된('Spayed' or 'Neutered') 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회
*/
--REGEXP(''|'')
SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
FROM ANIMAL_INS I JOIN ANIMAL_OUTS O
    ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE (I.SEX_UPON_INTAKE LIKE '%Intact%') AND (O.SEX_UPON_OUTCOME LIKE '%Spayed%' OR O.SEX_UPON_OUTCOME LIKE '%Neutered%')
ORDER BY O.ANIMAL_ID

/* SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
FROM ANIMAL_INS I RIGHT JOIN ANIMAL_OUTS O
    ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE <> O.SEX_UPON_OUTCOME
ORDER BY O.ANIMAL_ID */