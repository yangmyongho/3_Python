'''
step04, 05 문제 

 문1) 중복 되지 않은 직위 출력 하시오.
 문2) 각 직위별 빈도수를 출력하시오.
 
 <<출력 결과 >>
 중복되지 않은 직위 : ['사장', '과장', '대리', '부장'] : list -> set -> list
 각 직위별 빈도수 : {'과장': 2, '부장': 1, '대리': 2, '사장': 1} -> dict  
'''

position = ['과장', '부장', '대리', '사장', '대리', '과장']
    
# 문1)
position = set(position)
position = list(position)
print(position) # ['부장', '대리', '사장', '과장']

wc = {}
for pos in position :
    wc[pos] = wc.get(pos, 0) + 1
print(wc) # {'과장': 2, '부장': 1, '대리': 2, '사장': 1}