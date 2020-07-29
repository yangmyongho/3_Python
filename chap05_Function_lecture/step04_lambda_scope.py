'''
1. 축약함수(lambda)
 - 한 줄 함수
 형식) 변수 = lambda 인수 : 리턴값
 ex) lambda x,y : x+y

2. scope
 - 전역변수, 지역변수(함수)

'''

# 1. 축약함수
def adder(x,y) :
    add = x+y
    return add
# lambda 함수를 사용해서 위함수를 한줄로 표현가능
add = lambda x,y : x+y
 # 리스트 내포에 활용 : [lambda x,y : x+y for 변수 in 열거형객체]
re = add(3,2)
print(re) # 5


# 2. scope
''' 전역변수 : 전지역에서 사용되는 변수
    지역변수 : 특정 지역(함수) 안에서만 사용되는 변수 '''
x = 50

# 지역변수
def local_func(x) :
    x # 지역변수
    x += 50 # x = 100 : 지역변수 < 값이 나오지않는다.>
    # 해당 함수가 종료되면 자동으로 소멸
local_func(x) # x = 50
print('x =', x) # x = 50

# 전역변수
def global_func() :
    global x # 전역변수
    x += 50 # x = 100 : 전역변수 <값이 나온다>
global_func() # x = 100
print('x =', x) # x = 100


























































































