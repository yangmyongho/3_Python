'''
step05 문제

문) price에는 과일 가게에 진열된 과일과 가격이 저장되어 있고, 
      buy에는 고객이 구매한 장바구니이다.
      
      list + for 형식1)을 적용하여 구매 상품 총 금액(tot_bill)을 계산하시오.      
'''

# 과일가게 진열 상품
price = {'사과':2000, '복숭아' : 3000, '딸기' : 2500}

# 구매 상품
buy = {'사과' : 3, '딸기' : 5}

# 구매 상품 총 금액 

# 내가한 1
print(price['사과'] * buy['사과'])

for i in price.values() :
    for v in buy.values() :
        print(i*v)
# 내가한2
tot_bill = sum([0 if i == '복숭아' else (price[i]*buy[i]) for i in price])
print('총 구매 금액 :',tot_bill)

# 선생님
tot_bill = [price[b]*buy[b] for b in buy]
print('총 구매 금액 :', sum(tot_bill))












