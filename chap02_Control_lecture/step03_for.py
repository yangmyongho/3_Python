'''
제어문 : 반복문(for)

for 변수 in 열거형 객체 :
    실행문
    실행문

열거형 객체(iterable) : string, list, tuple, set/dict
제너레이터 식 : 변수 in 열거형 객체( 원소 순회 -> 변수 넘김)
'''


# 1. string 열거형 객체 이용
string = "나는 홍길동 입니다."
print(len(string)) # 11

for s in string : # 11회
    print(s, end='/') # 나/는/ /홍/길/동/ /입/니/다/./
for s in string.split(sep=' ') : # 3회
    print(s, end='/') # 나는/홍길동/입니다./
for s in string.split() : # 3회  위와 같은결과
    print(s, end='/') # 나는/홍길동/입니다./


# 2. list 열거형 객체 이용
help(list) # <리스트 자체에는 산술연산자 사용 불가능>
# Help on class list in module builtins:
lst = [1, 2, 3, 4, 5, 10]
print(lst, type(lst), len(lst)) # [1, 2, 3, 4, 5, 10] <class 'list'> 6
lst2 = [] # 빈공간에 제곱을해서 넣어보려함
for i in lst :
    print(i, end='/') # 1/2/3/4/5/10/
    lst2.append(i**2) # append : 원소 추가 (순서 보장)
print("\nlst2:", lst2) # lst2: [1, 4, 9, 16, 25, 100]


# 3. range 열거형 객체 이용
'''
range(n) : 0 ~ n-1 정수 
range(start, stop) : start ~ stop-1 정수
range(start, stop, step) : start ~ stop-1 , step 정수
'''
num1 = range(10) # 0 ~ 9
num2 = range(1, 10) # 1 ~ 9
num3 = range(1,10, 2) # 1 3 5 7 9
print("num1 = ", num1, "\nnum2 = ", num2, "\nnum3 = ", num3) # 객체의 정보만 확인할수있다.
'''num1 =  range(0, 10) 
   num2 =  range(1, 10) 
   num3 =  range(1, 10, 2)'''
print("num1 = ", list(num1), "\nnum2 = ", list(num2), "\nnum3 = ", list(num3)) # list 를 사용해서 원소 확인가능
'''num1 =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
   num2 =  [1, 2, 3, 4, 5, 6, 7, 8, 9] 
   num3 =  [1, 3, 5, 7, 9]'''
# 아니면 for 문 사용해서 확인가능
for i in num1 :
    print(i, end=', ') # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
for i in num2 :
    print(i, end=', ') # 1, 2, 3, 4, 5, 6, 7, 8, 9,
for i in num3 :
    print(i, end=', ') # 1, 3, 5, 7, 9,


# 4. (list + range) 열거형 객체 이용
idx = list(range(5)) # 0 ~ 4
print(idx) # [0, 1, 2, 3, 4]
# 1 ~ 100 원소를 갖는 list 객체 생성
lst3 = list(range(1, 101, 1)) # range(start, stop-1, step)
print(lst3) # [1, 2, 3, 4, 5, 6, 7, 8, 9,10, ... 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

for i in idx :
    print("i =", i, end=' / ')
    print("i^2 =", i**2)
''' i = 0 / i^2 = 0
    i = 1 / i^2 = 1
    i = 2 / i^2 = 4
    i = 3 / i^2 = 9
    i = 4 / i^2 = 16 '''

# ex1) lst1에 1 ~ 100 까지 100개의 원소를 갖는 vector를 생성하고, lst2에 3의 배수만 저장하기
lst1 = list(range(1,101))
lst2 = []
for i in lst1 :
    if i % 3 == 0 :
        lst2.append(i)
print(len(lst1)) # 100
print(len(lst2)) # 33


# index 이용 : 분류정확도
y = [1, 0, 2, 0, 1] # 관측치 : 범주형(0, 1, 2)
y_pred = [1, 0, 2, 2, 2] # 예측치
size = len(y)
print(size) # 5

acc = 0 # 분류정확도
for i in range(size) :  # =range(5) : 0 ~ 4
    fit = int(y[i] == y_pred[i]) # int(True/False) -> 1/0
    acc += fit * 20 # 누적변수
print("분류정확도 =", acc) # 분류정확도 = 60


# 5. 이중 for 문

# 1) 구구단
for i in range(2, 10) : # i = 단수
    print("*** {}단 ***".format(i))
    for j in range(1, 10) : # j = 곱수
        print("%d * %d = %d"%(i, j, (i*j)))
    print() # line skip
# 똑같음
for i in range(2, 10) : # i = 단수
    print("*** %d단 ***"%i) # i 를 (i) 로 써도된다.
    for j in range(1, 10) : # j = 곱수
        print("%d * %d = %d"%(i, j, (i*j)))
    print() # line skip
# 똑같음
for i in range(2, 10) : # i = 단수
    print("*** %d단 ***"%(i)) # i 를 (i) 로 써도된다.
    for j in range(1, 10) : # j = 곱수
        print("%d * %d = %d"%(i, j, (i*j)))
    print() # line skip

# 2) 문자열 처리
''' 형식)
for 변수 in  문단 : # 문장 -> 문단
     for 변수 in 문장 : # 문장 -> 단어
'''

para = '''나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다.'''
sents = []
words = []
for sent in para.split('\n') : # 문장 -> 문단
    sents.append(sent) # 문장 저장
    for word in sent.split(' ') : # 문장 -> 단어
        words.append(word) # 단어 저장
print(sents)
print('문장 길이 :', len(sents))
print(words)
print('단어 길이 :', len(words))
''' ['나는 홍길동 입니다.', '주소는 서울시 입니다.', '나이는 35세 입니다.']
    문장 길이 : 3
    ['나는', '홍길동', '입니다.', '주소는', '서울시', '입니다.', '나이는', '35세', '입니다.']
    단어 길이 : 9 '''


# 제너레이터 식 : 변수 in 열거형 객체
'''
for 변수 in 열거형 객체 :
    -> 객체의 원소 수 만큼 반복
if 값 in 열거형 객체 :
    -> 객체의 원소 중에서 값이 있으면 True, 아니면 False
'''

search = input("검색 단어 입력 :")
if search in words :
    print("해당 단어 있음")
else:
    print("해당 단어 없음")
''' 검색 단어 입력 :>? 홍길동
    해당 단어 있음
    검색 단어 입력 :>? 이순신
    해당 단어 없음 '''










