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
n = 1260 #손님이 지불한 금액
count = 0 #거슬러줘야하는 동전의 개수

#큰 단위의 화폐부터 차례대로 확인
coin_types = [500,100,50,10]

for coin in coin_types: #화폐 종류만큼 반복
    count += n//coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    
print(count)
