'''
정규 표현식

[주요 메타문자]
. : 임의의 한 문자
.x : 임의의 한 문자 뒤에 x가 오는 문자열(ex : abc, mbc -> .bc)
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x. : x 다음에 임의의 한 문자가 오는 문자열(ex : t1, t2, ta -> t.)
x* : x가 0번 이상 반복
x+ : x가 1개 이상 반복
x? : x가 0 또는 1개 존재
x{m, n} : x가 m~n 사이 연속
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치
'''

st1 = '1234 abc홍길동 ABC_555_6 이사도시'
st2 = 'test1abcABC 123mbc 45test'
st3 = 'test^홍길동 abc 대한*민국 123$tbc'


# 방법 1)  전부 가져와서 메모리를 많이 차지함
import re  # 정규표현식 적용하는 모듈
'''  re.findall() 이렇게 사용 '''

# 방법 2)  필요한것만 불러와서 메모리를 많이 차지하지 않음
from re import findall, match, sub  # 형식: from 모듈 import 함수
'''  findall() 이렇게 사용 '''


# 1. findall
''' 형식) findall(pattern='메타문자 패턴', string='문자열') 
    - 주로 문자를 찾을때 사용 '''

# 1) 숫자 찾기
st1 = '1234 abc홍길동 ABC_555_6 이사도시'
print(re.findall('1234', st1)) # ['1234'] - list 로 반환
print(findall('[0-9]{3}', st1)) # ['123', '555'] <숫자3개가 나열된것> - list 로 반환
print(findall('[0-9]{3,}', st1)) # ['1234', '555'] <숫자3개이상이 나열된것> - list 로 반환
print(findall('\\d{3,}', st1)) # ['1234', '555'] <숫자3개이상이 나열된것> - list 로 반환
print(findall(r'\d{3,}', st1)) # ['1234', '555'] <숫자3개이상이 나열된것> - list 로 반환
''' '[0-9]' = '\\d' = r'd' '''

# 2) 문자열 찾기
print(findall('[가-힣]{3,}',st1)) # ['홍길동', '이사도시']
print(type(findall('[가-힣]{3,}',st1))) # <class 'list'>
print(findall('[a-z]{3}', st1)) # ['abc']
print(findall('[a-z|A-Z]{3}', st1)) # ['abc', 'ABC']  < or 사용해서 소문자 대문자 둘다 검색 >

# 3) 단어찾아보기
str_list = st1.split() # 공백 단위로 짜르기
print(str_list) # ['1234', 'abc홍길동', 'ABC_555_6', '이사도시']
names = [] # 빈 리스트
for s in str_list :
    tmp = findall('[가-힣]{3,}', s)
    print(tmp)
    if tmp : # [] -> False , ['내용'] -> True
        names.append(tmp[0]) # ['홍길동', '이사도시'] < 단일 list >
        # names.append(tmp) # [['홍길동'],['이사도시']] <index를 안하면 중첩 list로 된다.>
print(names, type(names)) # ['홍길동', '이사도시'] <class 'list'>

# 4) 접두어/접미어 문자열 찾기
st2 = 'test1abcABC 123mbc 45test'
print(findall('test', st2)) # ['test', 'test']
print(findall('^test', st2)) # ['test']
print(findall('st$', st2)) # ['st']
# 종료 문자 찾기
print(findall('.bc', st2)) # ['abc', 'mbc']
# 시작 문자 찾기
print(findall('t.', st2)) # ['te', 't1', 'te']

# 5) 단어 찾기(\\w) : 한글, 영문자, 숫자
st3 = 'test^홍길동 abc 대한*민국 123$tbc'
words = findall('\\w{3,}', st3) # list 반환
print(words) # ['test', '홍길동', 'abc', '123', 'tbc']

# 6) 특정 문자열 제외
print(findall('[^t]+', st3)) # ['es', '^홍길동 abc 대한*민국 123$', 'bc']
print(findall('[^t]', st3)) # < + 를 생략하면 > t 를 제외한 글자 하나하나 전부 검색
''' ['e', 's', '^', '홍', '길', '동', ' ', 'a', 'b', 'c', ' ', '대', '한', '*', '민',
     '국', ' ', '1', '2', '3', '$', 'b', 'c'] '''
# 특수문자 제외
print(findall('[^^*$]+', st3)) # ['test', '홍길동 abc 대한', '민국 123', 'tbc']


# 2. match
''' 형식) match(pattern = '패턴', string = '문자열' 
    - 패턴 일치 여부 반환 (일치 : object 반환 , 불일치 : NULL 반환)  '''

jumin = "123456-1234567" # 정상적인 주민번호입니다.
jumin = "123456-5234567" # 비정상적인 주민번호입니다.
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin) # [0-9] = \\d
if result :  # object
    print("정상적인 주민번호입니다.")
else :  # None(NULL)
    print("비정상적인 주민번호입니다.")
print(result[0])

# 3. sub
''' 형식) sub('pattern', 'rep', 'string') 
    - 주로 전처리 할때 사용 '''

st3 = 'test^홍길동 abc 대한*민국 123$tbc'
# 특수문자 제외 < findall보다 보기 좋다. >
result = sub('[\^*$]', '', st3) #  \의미 : 메타문자가 아닌 일반 특수문자로 만듬
print(result) # test홍길동 abc 대한민국 123tbc














