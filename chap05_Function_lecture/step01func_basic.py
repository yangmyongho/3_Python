'''
함수(Function)
 - 중복 코드 제거
 - 재사용 가능
 - 특정 기능 1개 정의
 - 유형) 사용자 정의 함수, 라이브러리 함수
'''


# 1. 사용자 정의 함수
''' 형식) 
def 함수명(매개변수) : 
    실행문
    실행문
    [return 값1, 값2, ...] '''

# 1) 인수가 없는 기본 함수
def userFunc1() :
    print('인수가 없는 함수')
    print('userFunc1')
userFunc1() # 함수 호출

# 2) 인수가 있는 함수
def userFunc2(x, y):
    adder = x + y
    print('adder =', adder)
userFunc2(10, 20) # adder = 30

# 3) 리턴 있는 함수
def userFunc3(x, y) :
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return add, sub, mul, div
userFunc3(100, 20) # (120, 80, 2000, 5.0)
a,s,m,d = userFunc3(100, 20)
print('add =',a)
print('sub =', s)
print('mul =', m)
print('div =', d)


# 2. 라이브러리 함수
''' 
1) built-in : 기본 함수()
2) import : 모듈명.함수()  
'''

# 1) built-in : 기본 함수()
dataset = list(range(1,6))
print(dataset)
print('sum = ', sum(dataset)) # sum =  15
print('max =', max(dataset)) # max = 5
print('min =', min(dataset)) # min = 1
print('len =', len(dataset)) # len = 5
dir(sum) # 해당 모듈의 정보

# 2) import : 모듈명.함수()
import statistics # 통계관련 함수 제공  < 방법 1 >
from statistics import mean # 통계관련함수에서 mean 만 제공 < 방법 2 >
avg1 = statistics.mean(dataset)
avg2 = mean(dataset)
print('avg1 =', avg1) # avg1 = 3
print('avg2 =', avg2) # avg2 = 3

print(dir(statistics)) # 해당 모듈의 정보
''' ctrl + 클릭 : module or function source 보기 '''



