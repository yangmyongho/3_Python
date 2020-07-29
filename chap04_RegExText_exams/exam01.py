'''
문1) 다음 emp '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하시오. 

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''

from re import findall

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]





print('names =', findall('[가-힣]{3}', emp[0])) # names = ['홍길동']
##### 여기 내가한  for 문 이용
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]
EMP = []
for i in emp :
    EMP.append(findall('[가-힣]{3}', i)[0])
print('names =',EMP)


## 선생님 1) for 문 이용
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]
re = []
EMP = []
for i in emp :
    re = findall('[가-힣]{3}', i)
    EMP.append(re[0])
print('names =',EMP)


## 선생님 2) list + for 이용한 경우 : 변수 = [실행문 for 변수 in 열거형객체]
names = [findall('[가-힣]{3}', e)[0] for e in emp]
print('names =',names)