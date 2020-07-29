'''
제어문 : 조건문(if)

python 블럭 : 콜론과 들여쓰기
python 라인 : 한줄로 쓰기
'''


# 형식1) <탭키>
'''
if 조건식 : 
    실행문 
    실행문
'''
var = 10
if var >= 10 :
    print('var =', var)
    print('var는 10보다 크거나 같다.')
print('항상 실행되는 영역')
'''var = 10
var는 10보다 크거나 같다.
항상 실행되는 영역'''

if var >= 15 :
    print('var =', var)
    print('var는 10보다 크거나 같다.')
print('항상 실행되는 영역') # 항상 실행되는 영역


# 형식2)
'''
if 조건식 : 
    실행문1
else : 
    실행문2
'''
var = 2
if var >= 5 :
    print('var는 5보다 크거나 같다.')
else:
    print('var는 5보다 작다.')
'''var는 5보다 작다.'''

# ex1) 키보드 점수 입력 -> 60점 이상 : 합격, 미만 : 불합격
score = int(input("점수 입력 : "))
if score >= 60 :
    print('합격')
else :
    print('불합격')

# import 함수 사용한 if 문
import datetime # module 임포트 < 이거부터 해야한다. datetime을 가져온다.>
today = datetime.datetime.now() # module.class.method()
print(today) # 2020-04-07 11:10:30.292572
week = today.weekday()
print(week) # 1  < 0 ~ 4 : 평일, 5~6 : 휴일 >
if week >= 5 :
    print('오늘은 휴일이다.')
else:
    print('오늘은 평일이다.')
'''오늘은 평일이다.'''


# 형식3) # 조건식1이 참이면 실행문1, 조건식1이 거짓이고 조건식2가 참이면 실행문2, 조건식2도 거짓이면 실행문3
'''
if 조건식1 : 
    실행문1
elif 조건식2 : 
    실행문2
else : 
    실행문3
'''

# ex2) 키보드 score 입력 : A(100~90), B(80~89), C(70~79), D(60~69), F(59점 미만)
score = int(input("점수 입력 : "))
if score >= 90 :
    print('A학점')
elif score >= 80 :
    print('B학점')
elif score >= 70 :
    print('C학점')
elif score >= 60 :
    print('D학점')
else :
    print('F학점')
''' 점수 입력 : >? 75   C학점
점수 입력 : >? 88   B학점'''

# 전역변수 : score, grade
score = int(input("점수 입력 : "))
grade = ''
if score >= 90 :
    grade = 'A학점'
elif score >= 80 :
    grade = 'B학점'
elif score >= 70 :
    grade = 'C학점'
elif score >= 60 :
    grade = 'D학점'
else :
    grade = 'F학점'
print("당신의 점수는 %d이고, 등급은 %s이다."%(score, grade))
'''점수 입력 : >? 85
당신의 점수는 85이고, 등급은 B학점이다.'''


# 형식4) 블럭 if  vs  라인 if
'''블럭 if '''
num = 9
if num >= 5 :
    result = num * 2
else:
    result = num + 2
print(result) # 18

'''
라인 if 
형식) 변수 = 참 if 조건문 else 거짓
'''
num = 3
result =num * 2 if num >= 5 else num + 2
print(result) # 5











