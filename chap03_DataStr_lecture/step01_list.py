'''
list 특징
 - 1차원 배열 구조
   형식) 변수 = [값1, 값2, ...]
 - 다양한 자료형 저장 가능
 - index 사용, 순서 존재
   형식) 변수[index], index의 시작은 0부터
 - 값 수정 가능 (추가, 삽입, 수정, 삭제)
'''


# 1. 단일 list
lst = [1, 2, 3, 4, 5]
print(lst, type(lst), len(lst)) # [1, 2, 3, 4, 5] <class 'list'> 5

for i in lst :
    print(i, end='/') # 1/2/3/4/5/

for i in lst:
        print(lst[i-1: ]) # 변수[start : stop]

for i in lst :
    print(lst[ :i]) # 변수[start : stop]

# 처음 / 마지막 데이터 추출
x = list(range(1,101)) # 1 ~ 100
print(x)
print(x[:5]) # [1, 2, 3, 4, 5] <앞부분 5개 원소>
print(x[-5:]) # [96, 97, 98, 99, 100] <마지막 5개 원소>
print(x[95:]) # [96, 97, 98, 99, 100] <위와 같음>
'''
index 형식
변수[start : stop-1 : step]
 < start 가 stop 보다 클경우 step자리에는 음수가 와야한다. >
'''
print(x[:]) # 전체
print(x[::2]) # [::step=2] 1부터 2씩 증가하는 전체 = < 홀수 >
print(x[1::2]) # [start=1::step=2] 2부터 2씩 증가하는 전체 = < 짝수 >


# 2. 중첩 list : [[], []] -> 1차원
a = ['a', 'b', 'c']
b = [10, 20, a, 5, True, "hong"] # 서로 다른 type 가능 , 리스트안에 리스트 삽입 가능
print(b) # [10, 20, ['a', 'b', 'c'], 5, True, 'hong']
print(b[2]) # ['a', 'b', 'c']
# 'b'만 꺼내고싶을때
print(b[2][1]) # b  < 중첩 list를 꺼내올 경우 >
print(b[2][1:]) # ['b', 'c']
print(b[1], b[2][0], b[2][2], b[3]) # 20 a c 5

print(type(a), type(b)) # <class 'list'> <class 'list'>
print(id(a), id(b)) # 2293207520328 2293207475912 < a와b 는 주소가다르지만>
print(id(a), id(b[2])) # 2293207520328 2293207520328 <b의 2번째 인덱스값은 a와  같으므로 주소도 같다>


# 3. 값 수정 (추가, 삽입, 수정, 삭제)
num = ['one', 'two', 'three', 'four']
print(len(num), type(num)) # 4 <class 'list'>

# 원소 추가 <순서 제일끝>
num.append('five')
print(num) # ['one', 'two', 'three', 'four', 'five']

# 원소 삭제
num.remove('five')
print(num) # ['one', 'two', 'three', 'four']

# 원소 삽입 <순서 지정>
num.insert(0, 'zero')
print(num) # ['zero', 'one', 'two', 'three', 'four']

# 원소 수정 <index로 수정할자리 = 수정할값>
num[0] = 0
print(num) # [0, 'one', 'two', 'three', 'four']


# 4. list 연산( + , * )
x = [1, 2, 3, 4]
y = [1.5, 2.5]

# 1) list 결합(+)
z = x + y # new object
print(z) # [1, 2, 3, 4, 1.5, 2.5] - 단일 list

# 2) list 확장
x.extend(y) # 기존 object
print(x) # [1, 2, 3, 4, 1.5, 2.5] - 단일 list

# 3) list 추가
x.append(y) # 기존 object
print(x) # [1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]] - 중첩 list

''' 결합과 확장의 차이점 : new , 기존
    결합과 추가의 차이점 : new , 기존
    확장과 추가의 차이점 : 단일 list , 중첩 list '''

# 4) list 곱셈(*)
lst = [1, 2, 3, 4]
result = lst*2 # 2번 반복
print(result) # [1, 2, 3, 4, 1, 2, 3, 4]


# 5. list 정렬
result.sort() # 생략시 오름차순
result.sort(reverse=False) # 오름차순
print(result) # [1, 1, 2, 2, 3, 3, 4, 4]
result.sort(reverse=True) # 내림차순
print(result) # [4, 4, 3, 3, 2, 2, 1, 1]


# 6. scala  vs  vector
''' scala 변수 : 한 개의 상수(값)을 갖는 변수(크기)
    vector 변수 : 다수의 상수(값)을 갖는 변수(크기, 방향) '''

dataset = [] # 빈 list
size = int(input("vector size :")) # scala 변수
for i in range(size) : # range(5) : 0 ~ 4 < 5번 반복 >
    dataset.append(i+1) # vector 변수
print(dataset) # [1, 2, 3, 4, 5]


# 7. list에서 원소 찾기
''' if 값 in list :
        참 실행문
    else : 
        거짓 실행문 '''

if 5 in dataset :
    print("5가 있음")
else:
    print("5가 없음")
 # 5가 있음


