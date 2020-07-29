'''
클래스(class)
 - 함수의 모임
 - 역할 : 다수의 함수와 공유 자료를 묶어서 객체(object) 생성
 - 유형 : 사용자정의 클래스 , 라이브러리 클래스(python)
 - 구성 요소 : 멤버(member) + 생성자
 - 멤버(member) : 변수(자료 저장) + 메서드{=함수}(자료 처리)
 - 생성자 : 객체 생성 + 멤버변수값 초기화
 - 함수와의 차이점 <1. 객체의 생성 유무> , <2. def 로 시작하지않고 class 로 시작함>
 형식)
 class 클래스명 :
    멤버변수 = 자료
    생성자(self, 객체 생성) :
        멤버변수값 초기화
    def 멤버메서드(self) :
        자료처리
'''


# 1. 중첩함수
def calc_func(a, b) :
    # outer : 자료저장
    x = a
    y = b

    # inner : 자료조작(처리)
    def plus() :
        return x + y
    def minus() :
        return x - y
    return plus, minus

p, m = calc_func(10, 20) # 일급함수
print('plus =', p()) # plus = 30
print('minus =', m()) # minus = -10


# 2. 클래스 정의
class calc_class:
    # 멤버변수(전역변수) : 자료저장
    x = y = 0

    # 생성자 : 객체생성 + 멤버변수값 초기화
    def __init__(self, a, b): # 객체생성
        # 멤버변수값 초기화 < self.멤버변수 = 지역변수 >
        self.x= a
        self.y = b

     # 멤버메서드 : 클래스에서 정의한 함수
    def plus(self):
        return self.x + self.y
    def minus(self):
        return self.x - self.y

''' 클래스(1) vs 객체(n) '''
# 생성자 -> 객체1(object)
obj1 = calc_class(10, 20) # 클래스명() : 생성자 -> 객체생성
# object.member : 멤버변수 호출
print('x =', obj1.x) # x = 10
print('y =', obj1.y) # y = 20
# object.member() : 멤버메서드 호출
print('plus =', obj1.plus()) # plus = 30
print('minus =', obj1.minus()) # minus = -10

# 생성자 -> 객체2(object)
obj2 = calc_class(100, 50) # 클래스명() : 생성자 -> 객체생성
# object.member : 멤버변수 호출
print('x =', obj2.x) # x = 100
print('y =', obj2.y) # y = 50
# object.member() : 멤버메서드 호출
print('plus =', obj2.plus()) # plus = 150
print('minus =', obj2.minus()) # minus = 50

# 객체 주소 확인 <서로다른주소>
print('obj1 =', id(obj1), 'obj2 =', id(obj2)) # obj1 = 1923889496264 obj2 = 1923889499336


# 3. 라이브러리 클래스
from datetime import date # from 모듈 import 클래스
today = date(2020, 4, 13) # 생성자 -> 객체생성

# object.member
print('year :', today.year) # year : 2020
print('month :', today.month) # month : 4
print('day :', today.day) # day : 13

# object.member()
print('week :', today.weekday()) # week : 0(-> 월요일)















