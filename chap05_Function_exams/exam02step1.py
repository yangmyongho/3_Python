'''
문2-1) 다음 벡터(emp)는 '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하는 함수를 정의하시오. 

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''

from re import findall

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]
print(emp)

# 함수 정의


# 내가한
def name_pro(emp):
    from re import sub
    nn = []
    for i in emp :
        n_m = sub('[0-9]','',i)
        nn.append(n_m)
    return nn
# 함수 호출 
names = name_pro(emp)
print('names =', names)



###선생님
def name_pro(emp):
    names = []
    for e in emp :
        tmp = findall('[가-힣]{3}',e)
        if  tmp :
            names.append(tmp[0])
    return names
# 함수 호출
names = name_pro(emp)
print('names =', names)


### 리스트내포
mame = [findall('[가-힣]{3}',e)[0] for e in emp ]
print('names =',mame)







