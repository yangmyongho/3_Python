'''
문) emp.csv 파일을 읽어와서 다음 출력 예시와 같이 처리하시오. 
 
       <<출력 예시>>
관측치 길이 :  5
전체 평균 급여 : 370.0
==============================
최저 급여 : 150, 이름 : 홍길동
최고 급여 : 500, 이름 : 강감찬
==============================
'''
import pandas as pd

# 1. file read
emp = pd.read_csv('./chap07_FileIO/data/emp.csv', encoding='utf-8')
print(emp.info())
print(emp)


print('관측치 길이 :', len(emp))
print('전체 평균 급여 :', emp['Pay'].mean())
print('='*30)
for i in range(5) :
    if emp['Pay'][i] == min(emp['Pay']) :
        print('최저 급여 : {}, 이름 : {}'.format(emp['Pay'][i], emp['Name'][i]))
    elif emp['Pay'][i] == max(emp['Pay']) :
        print('최고 급여 : {}, 이름 : {}'.format(emp['Pay'][i], emp['Name'][i]))
print('='*30)

# 추가 상식
for idx, num in enumerate(emp.Pay):
    print(idx)
    print(num)


print(emp.shape) # (5, 3) < tuple형식 > index 사용가능
print(emp.shape[0]) # 5
print(emp.shape[1]) # 3