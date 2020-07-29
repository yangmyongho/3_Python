'''
중첩함수 -> 클래스(data + function)
'''

class Account: # outer -> class
    # outer변수 -> 멤버변수
    balance = 0  # 잔액(balance) <없어도됌>

    # 생성자
    def __init__(self, bal):
        self.balance = bal # 멤버변수 초기화

    # inner -> 멤버메서드
    def getBalance(self):  # 잔액확인(getter)
        return self.balance

    def deposit(self, money):  # 입금하기(setter)
        if money < 0:
            print("금액을 확인하세요.")
        else:
            # nonlocal balance < nonlocal -> self >
            self.balance += money

    def withdraw(self, money):  # 출금하기(setter)
        # nonlocal balance < nonlocal -> self >
        if self.balance < money:
            print("잔액이 부족합니다.")
        else:
            self.balance -= money

acc = Account(1000)
print('잔액 :',acc.getBalance()) # 잔액 : 1000
acc.deposit(2000)
print('잔액 :',acc.getBalance()) # 잔액 : 3000
acc.withdraw(500)
print('잔액 :',acc.getBalance()) # 잔액 : 2500
acc.withdraw(5000) # 잔액이 부족합니다.
acc.deposit(-500) # 금액을 확인하세요.

'''
1. 예금자(accName), 계좌번호(accNo) 동적 멤버변수 추가하기
    -> 예금자 : 홍길동 , 계좌번호 : 010-125-41520
2. getBalance() 메서드를 이용하여 잔액, 예금주, 계좌번호 출력하기

'''
class Account2: # outer -> class
    # outer변수 -> 멤버변수
    balance = 0  # 잔액(balance) <없어도됌>

    # 생성자
    def __init__(self, bal, accName, accNo):
        self.balance = bal # 멤버변수 초기화
        self.accName = accName
        self.accNo = accNo

    # inner -> 멤버메서드
    def getBalance(self):  # 잔액확인(getter)
        return self.balance, self.accName, self.accNo

    def deposit(self, money):  # 입금하기(setter)
        if money < 0:
            print("금액을 확인하세요.")
        else:
            # nonlocal balance < nonlocal -> self >
            self.balance += money

    def withdraw(self, money):  # 출금하기(setter)
        # nonlocal balance < nonlocal -> self >
        if self.balance < money:
            print("잔액이 부족합니다.")
        else:
            self.balance -= money

acc3 = Account2(1000,'홍길동', '010-125-41520')
acc3.getBalance() # (1000, '홍길동', '010-125-41520')
re, name, acc = acc3.getBalance()
print('이름 :', name, ', 계좌번호 :', acc, ', 잔액 :', re)
# 이름 : 홍길동 , 계좌번호 : 010-125-41520 , 잔액 : 1000
acc3.deposit(50000)
re, name, acc = acc3.getBalance()
print('이름 :', name, ', 계좌번호 :', acc, ', 잔액 :', re)
# 이름 : 홍길동 , 계좌번호 : 010-125-41520 , 잔액 : 51000






