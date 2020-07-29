'''
함수의 가변인수
 - 한 개의 가인수로 여러 개의 실인수를 받는 인수
 형식) def 함수명(*인수)
'''


# 1. tuple형 으로 받는 가변인수
def Func1(name, *names) :
    print(name)
    print(names)
Func1('홍길동', '이순신', '유관순')
''' 홍길동
    ('이순신', '유관순') '''

# 패키지 모듈
''' 방법1) import 패키지.모듈 '''
import scatter.scatter_module
''' 방법2) from 패키지.모듈 import 함수1, 함수2, 클래스1, 클래스2 '''
from scatter.scatter_module import Avg, var_std

datas = [2, 3, 5, 6, 7, 8.5]
avg1 = scatter.scatter_module.Avg(datas) # 방법1)
print(avg1) # 5.25
avg2 = Avg(datas) # 방법2)
print(avg2) # 5.25
var, std = var_std(datas) # 방법2)
print('var =', var) # var = 5.975
print('std =', std) # std = 2.444381312316063

def statis(func, *data):
    if func == 'sum' :
        return sum(data) # 함수 실행 종료 (exit)
    if func == 'avg' :
        return Avg(data)
    if func == 'var' :
        return var_std(data)
    if func == 'std' :
        return var_std(data)
print('sum =', statis('sum', 1,2,3,4,5)) # sum = 15
print('avg =', statis('avg', 1,2,3,4,5)) # avg = 3
var, _ = statis('var', 1,2,3,4,5)
print('var =', var) # var = 2.5
_, std = statis('var', 1,2,3,4,5)
print('std =', std) # std = 1.5811388300841898


# 2. dict형 가변인수 <**부분을 딕셔너리로 묶어버림>
def person(w, h, **other) :
    print('w =', w)
    print('h =', h)
    print(other)
person(65,175, name='홍길동', age=35)
''' w = 65
    h = 175
    {'name': '홍길동', 'age': 35} '''


# 3. 함수를 인수로 받기
def square(x):
    return x**2
def my_func(func, datas):
    result = [func(d) for d in datas]
    return result
data = [1,2,3,4,5]
print(my_func(square, data)) # [1, 4, 9, 16, 25]  <형식 : (함수, 데이터셋)>


'''
내가하던
def square(x):
    return x**2
def my_func(func, datas):
    result = [square(d) for d in datas]
print(square(data))
'''





























































