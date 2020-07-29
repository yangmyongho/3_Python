'''
 <급여 계산 문제>
문4) Employee 클래스를 상속하여 Permanent와 Temporary 클래스를 완성하시오.     
'''

# 부모클래스 
class Employee : 
    name = None
    pay = 0
    def __init__(self,name):
        self.name = name

# 자식클래스 - 정규직 
class Permanent(Employee):
    gi = bonus = 0
    def __init__(self, name, gi, bonus):
        super().__init__(name)
        # self.gi = gi < 간단하게 생략가능 >
        # self.bonus = bonus
        # self.pay = self.gi + self.bonus
        self.pay = gi + bonus

# 자식클래스 - 임시직 
class Temporary(Employee):
    time = tpay = 0
    def __init__(self, name, time, tpay):
        Employee.__init__(self, name)
        # self.time = time < 간단하게 생략가능 >
        # self.tpay = tpay
        # self.pay = self.time * self.tpay
        self.pay = time * tpay


empType = input("고용형태 선택(정규직<P>, 임시적<T>) : ")
if empType == 'P' or empType == 'p' :
    name = input('이름 : ')
    gi = int(input('기본급 : '))
    bonus = int(input('상여금 : '))
    p = Permanent(name, gi, bonus)
    print('='*30)
    print('고용형태 : 정규직')
    print('이름 : ', p.name)
    print('급여 : ', format(p.pay, '3,d'))
elif empType == 'T' or empType == 't' :
    name = input('이름 : ')
    time = int(input('작업시간 : '))
    tpay = int(input('시급 : '))
    t = Temporary(name, time, tpay)
    print('='*30)
    print('고용형태 : 임시직')
    print('이름 : ', t.name)
    print('급여 : ', format(t.pay, '3,d'))
else :
    print('='*30)
    print('입력 오류')

'''
==============================
고용형태 : 정규직
이름 :  홍길동
급여 :  2,300,000
==============================
고용형태 : 임시직
이름 :  유관순
급여 :  675,000
===========================
입력 오류
'''

