'''
예외 : 프로그램 싱행상태에서 예기치 않은 상황(오류)
try :
    예외발생 코드
except :
    예외처리 코드
finally(생략가능) :
    항상처리 코드
'''


# 1. 간단한 예외처리
# 1-1) 정상 프로그램
print('프로그램 시작')
x=[10, 20, 'num', 14.5]
for i in x :
    print('x =', i, end=' / ')
    y = i*2
    print('y =', y)
print('프로그램 종료')
'''
프로그램 시작
x = 10 / y = 20
x = 20 / y = 40
x = num / y = numnum
x = 14.5 / y = 29.0
프로그램 종료
'''

# 1-2) 예외발생 확인
print('프로그램 시작')
for i in x :
    print('x =', i, end=' / ')
    y = i**2
    print('y =', y)
print('프로그램 종료')
'''
프로그램 시작
x = 10 / y = 100
x = 20 / y = 400
x = num /  # 여기서 중단되어서 14.5와 14.5의 제곱은 나오지 못했다.
뒷부분은 실행할수없다.
'''

# 1-3) 예외처리
print('프로그램 시작')
for i in x :
    try :
        print('x =', i, end=' / ')
        y = i**2
        print('y =', y)
    except :
        print('y = 예외발생 :', i, '(숫자 아님)')
print('프로그램 종료')
'''
프로그램 시작
x = 10 / y = 100
x = 20 / y = 400
x = num / y = 예외발생 : num (숫자 아님)
x = 14.5 / y = 210.25
프로그램 종료
'''


# 2. 유형별 예외처리
# 2-1) 정상 프로그램
print('유형별 예외처리')
try:
    div = 1000 / 2.5 # 정상
    print('div = %.3f'%div)
except:
    print('예외발생')
finally:
    print('프로그램 종료')
'''
유형별 예외처리
div = 400.000
프로그램 종료
'''

# 2-2) 산술적 예외처리 <ZeroDivisionError>
print('유형별 예외처리')
try:
    div = 1000 / 2.5 # 정상
    print('div = %.3f'%div)
    div2 = 1000 / 0 # 1차 : 산술적 예외(오류)
    print('div2 = %.3f' % div2)
except ZeroDivisionError as e: # class as object
    print('예외발생 :', e) # 예외발생 : division by zero
finally:
    print('프로그램 종료')
'''
유형별 예외처리
div = 400.000
예외발생 : division by zero
프로그램 종료
'''

# 2-3) 파일열기 예외처리 <FileNotFoundError>
print('유형별 예외처리')
try:
    div = 1000 / 2.5 # 정상
    print('div = %.3f'%div)
    f = open('c:/text.txt') # 2차 : 파일열기 예외(오류)
except FileNotFoundError as e : # file io 예외처리
    print('예외발생 :', e) # 예외발생 : [Errno 2] No such file or directory: 'c:/text.txt'
finally:
    print('프로그램 종료')
'''
유형별 예외처리
div = 400.000
예외발생 : [Errno 2] No such file or directory: 'c:/text.txt'
프로그램 종료
'''

# 2-4) 기타(만능) 예외처리 <Exception>
print('유형별 예외처리')
try:
    div = 1000 / 2.5 # 정상
    print('div = %.3f'%div)
    num = int(input("숫자 입력 :")) # 3차 : 기타 예외발생
    print('num =', num)
except Exception as e: # 나머지 예외처리
    print('예외발생 :', e) # 예외발생 : invalid literal for int() with base 10: '가'
finally:
    print('프로그램 종료')










