'''
dict 특징
 - set 구조와 유사하다. ( 순서 없음 = index 사용 불가)
 - R 의 list 와 유사하다.
 - key 와 value 한 쌍으로 원소 구성
 - key 를 통해서 value 참조한다.
 - key 중복은 불가 , value 중복 가능
 형식) 변수 = {key1:value1, key2:value2, key3:value2, ...}
'''


# 1. dict 생성
# 1) 방법1
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic, type(dic), len(dic))
# {'key1': 100, 'key2': 200, 'key3': 300} <class 'dict'> 3
dic = dict(a=1, b=2, c=3) # {'a': 1, 'b': 2, 'c': 3} <class 'dict'> 3

# 2) 방법2
dic2 = {'name':'홍길동', 'age':35, 'addr':'서울시'}
print(dic2, type(dic2), len(dic2))
# {'name': '홍길동', 'age': 35, 'addr': '서울시'} <class 'dict'> 3
dic2 = {'a':(1,2) , 'b':[2,3], 'c':3} # {'a': (1, 2), 'b': [2, 3], 'c': 3} <class 'dict'> 3


# 2. 수정, 추가, 삭제, 검색 : key 이용
dic2['age'] = 45 # 수정
dic2['pay'] = 350 # 추가
del dic2['addr'] # 삭제
print(dic2) # {'name': '홍길동', 'age': 45, 'pay': 350}
print('age' in dic2) # True # 키 검색


# 3. for 이용
# 키만 넘김
for k in dic2.keys() :
    print(k, end='/') # name/age/pay/

# 값만 넘김
for v in dic2. values() :
    print(v, end='/') # 홍길동/45/350/

# 둘 다 넘김
for k in dic2 : # dic2 = dic2.keys()
    print(k, end=':')
    print(dic2[k])
''' name:홍길동
    age:45
    pay:350 '''
# 둘 다 넘김
for k,v in dic2.items() :
    print(k, end=':')
    print(v)
''' name:홍길동
    age:45
    pay:350 '''


# 4. key -> value
print(dic2['name']) # 홍길동 <index 형식으로 불러온 결과>
print(dic2.get('name')) # 홍길동 <get() 으로 불러온 결과>


# 5. {'key' : [value1, value2]}  -> ex) {'이름' : [급여, 수당]}
emp = {'hong' : [250, 50], 'lee' : [350, 80], 'yoo' : [200, 40]}
print(emp) # {'hong': [250, 50], 'lee': [350, 80], 'yoo': [200, 40]}

for k, v in emp.items() : # key, value
    print(k, end=':')
    print(v)
''' hong:[250, 50]
    lee:[350, 80]
    yoo:[200, 40] '''

# ex1) 급여가 250 이상인 사원 정보 출력
for k, v in emp.items():
    if v[0] >= 250:
        print(k, end=':')
        print(v)
''' hong:[250, 50]
    lee:[350, 80] '''

# ex2) 급여가 250 이상인 경우 사원명, 수당 합계
su = 0
for k, v in emp.items():
    if v[0] >= 250: # 급여 비교 판단
        print(k)
        su += v[1] # 수당 누적
print('수당 합계 =', su)
''' hong
    lee
    수당 합계 = 130 '''


# 6. 문자 빈도수 구하기
charset  = ['love', 'test', 'love', 'hello', 'test', 'love']
print(len(charset)) # 6

# 방법 1)
wc = {} # 빈 set
for word in charset :
    if word in wc :
        wc[word] += 1 # 2회 이상 발견 : 1씩 증가
    else :
        wc[word] = 1 # 최초 발견 : 1을 초기화
print(wc) # {'love': 3, 'test': 2, 'hello': 1}
print(max(wc, key=wc.get)) # love

# 방법 2)
wc2 = {} # 빈 set
for word in charset :
    #   key   =  value
    wc2[word] = wc2.get(word, 0) + 1
print(wc2) # {'love': 3, 'test': 2, 'hello': 1}
print(max(wc2, key=wc2.get))
