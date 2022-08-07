/* 1
동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회, 이때 고양이를 개보다 먼저 조회 */
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) as count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC;


/* 2
동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회
이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회 */
SELECT NAME, COUNT(NAME)
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME ASC;


/* 3
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지
09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회, 이때 결과는 시간대 순으로 정렬 */
SELECT HOUR(DATETIME) as HOUR, COUNT(ANIMAL_ID) as COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING 20 > HOUR and HOUR >= 9 #HOUR BETWEEN 9 and 19  ( 20 > HOUR >= 9 형태의 표현식은 인식 못함) 
ORDER BY HOUR ASC;


/* 4 (다양한 풀이: SET으로 변수 선언, WITH로 SubQuery 정의 등)
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지
0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회, 이때 결과는 시간대 순으로 정렬 */
SET @hour = -1;

--ANIMAL_OUTS의 레코드는 총 100건이므로, @hour는 0부터 99까지 1씩 증가하는 값을 가지게 됨
SELECT (@hour := @hour +1) AS HOUR,
    (SELECT COUNT(ANIMAL_ID)
    FROM ANIMAL_OUTS
    WHERE HOUR(DATETIME) = @hour) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23;