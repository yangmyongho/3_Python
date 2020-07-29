'''
연산자(operator)
1. 변수에 값 할당(=)
2. 연산자 : 산술, 관계, 논리
3. print 형식
4. input : 키보드 입력
'''


# 1. 변수에 값 할당(=)

i = tot = 10
i += 1 # i = i + 1 : 카운터 변수
tot += i # tot = tot + i : 누적 변수
print('i= ', i) # i = 11
print('tot =', tot) # tot = 21

v1, v2 = 100, 200
print('v1 =', v1, 'v2 =', v2) # v1 = 100 v2 = 200
# 변수 값 교체
'''
tmp = v1
v1 = v2
v2 = tmp
'''
v1, v2 = v2, v1
print('v1 =', v1, 'v2= ', v2)

# 패킹(packing) 할당
lst = [1,2,3,4,5] # vector 할당
v1, *v2 = lst
print('v1 =', v1, 'v2 =', v2) # v1 = 1 v2 = [2,3,4,5]
*v1, v2 =lst
print('v1 =', v1, 'v2 =', v2) # v1 = [1, 2, 3, 4] v2 = 5


# 2. 연산자 : 산술, 관계, 논리

print("산술연산자")
num1 = 100 # 피연산자1
num2 = 20  # 피연산자2
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2 # 실수 몫
div2 = num1 // num2 # 정수 몫
div3 = num1 % num2 # 나머지값
square = num1**2 # 제곱값
print(add, sub, mul) # 120 80 2000
print(div, div2, div3) # 5.0 5 0
print(square) # 10000

print("관계연산자") # True or False
# 1) 동등비교
bool_re = num1 == num2
print(bool_re) # False
bool_re = num1 != num2
print(bool_re) # True
# 2) 대소관계 : >, >=, <, <=
bool_re = num1 >= num2
print(bool_re) # True
bool_re = num1 <= num2
print(bool_re) # False

print("논리연산자") # or, and, not
bool_re = num1 >= num2 or num1 <= 10
print(bool_re) # True
bool_re = num1 >= num2 and num1 <= 10
print(bool_re) # False
bool_re = (num1 <= 10)
print(bool_re) # False
bool_re = not(num1 <= 10) # not은 False -> True 로 변경해줌
print(bool_re) # True


# 3. print 형식
help(print)
# package > module > function or class
# Help on built-in function print in module builtins:
# print(value, ..., sep=' ', end='\n'
# module builtins : 기본 모듈(python 설치 시 자동으로 설치되는 모듈)
'''
함수의 인수
매개변수 : 값을 넘겨 받는 변수
파라미터 : 값을 갖는 변수
'''


#1) 기본 인수
print("values =", 10+20+30) # values = 60
print("출력1", end=', ')
print("출력2") # 출력1, 출력2
print("010", "1111", "2222", sep='-') # 010-1111-2222

# 2) format(value, '양식문자') # 양식문자(p.22)
print("원주율=", format(3.14159, "8.3f") ) # 원주율=    3.142
print("금액 =", format(10000, "10d")) # 금액 =      10000
print("금액 =", format(125000, "3,d")) # 금액 = 125,000

# 3) print("양식문자" % (값))
num1 = 10; num2 = 20
tot = num1 + num2
print("%d + %d = %d" %(num1, num2, tot)) # 10 + 20 = 30
print("8진수 = %o, 16진수 = %x" %(num1, num2)) # 8진수 = 12, 16진수 = 14
print("%s = %8.5f" %("PI", 3.14159)) # PI =  3.14159 <8자리수, 소수점 5자리>

# 4) 외부 상수 받기
# "{}, {}".format(value1, value2)
print("name : {}, age : {}".format("홍길동", 35)) # name : 홍길동, age : 35
print("name : {1}, age : {0}".format("홍길동", 35)) # name : 35, age : 홍길동 <숫자는 0부터>
print("name : {}, age : {}")

# format  축약형 : sql
# <select * from emp where name = '홍길동' and age = 35> 만들기
name = "홍길동"
age = 35
sql = f"select * from emp where name = '{name}' and age = {age}"
print(sql) # select * from emp where name = '홍길동' and age = 35


# 4. input("prompt") : 키보드 입력 (문자로 인식)<str>
'''
int(value) : value -> intrger
float(value) : value -> float
str(value) : value -> string
'''
a = input("첫번째 숫자 입력 : ") # 첫번째 숫자 입력 : >? 10
b = input("두번째 숫자 입력 : ") # 두번째 숫자 입력 : >? 20
print("a + b = ", a+b) # a + b =  1020
# int 사용 숫자형식으로 변경
a = int(input("첫번째 숫자 입력 : ")) # 첫번째 숫자 입력 : >? 10
b = int(input("두번째 숫자 입력 : ")) # 두번째 숫자 입력 : >? 20
print("a + b = ", a+b) # a + b =  30
# float 사용 실수형으로 변경
a = float(input("첫번째 숫자 입력 : ")) # 첫번째 숫자 입력 : >? 12.243
b = float(input("두번째 숫자 입력 : ")) # 두번째 숫자 입력 : >? 12
print("a + b = ", a+b) # a + b =  24.243000000000002
print('b =', b) # b = 12.0
print('a =', a) # a = 12.243
print(type(b)) # <class 'float'>

# boolen -> int
print(int(False)) # 0
print(int(True)) # 1
# int -> boolen
print(bool(0)) # False
print(bool(1)) # True
print(bool(3)) # True < 0 이 아닌모든숫자는 True >







