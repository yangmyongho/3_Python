'''
중첩함수 (inner function)
 형식)
 def outer_func(인수) :
    실행문
    def inner_func(인수) :
        실행문
    return inner_func
'''


# 1. 중첩함수 예
def a() : # outer
    print('a 함수')
    def b() : # inner
        print('b 함수')
    return b # inner func

a() # outer 호출
''' a 함수
    <function a.<locals>.b at 0x000001DA128175E8> '''
b = a() # a 함수   <outer 호출 - a 함수 = 일급함수>
b() # b 함수   <inner 호출 - b 함수>


# 2. 중첩함수 응용
''' inner 함수 종류 
    getter() : 함수내 data를 외부로 획득하는 획득자
    setter() : 함수내 data를 조작하는 지정자  '''

def outer_func(data) : # outer 역할 : 데이터 저장, inner 포함
    dataSet = data

    # inner 역할 : 데이터 조작
    def tot(): # 합계
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val): # 평균 = 합계/n
        avg_val = tot_val / len(dataSet)
        return avg_val

    # getter
    def getData() :
        return dataSet

    # setter
    def setData(newData) :
        nonlocal dataSet # outer 변수 <nonlocal : 전역변수로 만들어줌>
        dataSet = newData # 원래는 지역변수였지만 전역변수로 변경했다.

    return tot, avg, getData, setData

data = list(range(1,101))
newData = list(range(1,51))
tot, avg, getData, setData = outer_func(data) # 일급함수(tot, avg)

tot_val = tot() # 합계 계산
avg_val = avg(tot_val) # 평균 계산
print('tot =', tot_val) # tot = 5050
print('avg =', avg_val) # avg = 50.5
print('dataset =', getData()) # dataset 리턴
setData(newData) # dataset 변경
# getter 이용 : dataset 확인
print('setdata =', getData()) # 변경된 dataset 리턴


# 3. 함수 장식자 : Tensorflow2.0 에서 적용
''' - 기존 함수의 시작부분과 종료부분에 기능을 추가해서 장식 역할
    @함수장식자
    def 함수명() :
        실행문                                             '''

# 함수장식자 작성
def hello_deco(func) : # outer함수 :함수를 인수로 받는 역할
    def inner(name) : # inner함수 : 함수 장식하는 역할 <hello인수 받음>
        print('-'*30) # 함수 앞부분 데코
        func(name) # 함수 실행
        print('-'*30) # 함수 뒷부분 데코
    return inner

@hello_deco
def hello(name) :
    print('my name is ' + name + '!!!')

# 함수 호출
hello('홍길동')


# 구구단 장식하기
''' **** 2단 ****
    2 * 1 = 2
     ...
    2 * 9 = 18
    ***********                        '''

# 공통
def gugu_deco(gugu_func):
    def inner(dan):
        print('**** ', dan, '단 ****')
        gugu_func(dan)
        print('*'*15)
    return inner

# 내가한
@gugu_deco
def gugu(dan):
    num = 0
    while True :
        if num <= 9 :
            num += 1
            print(dan, '*', num, ' = ', dan*num)
        else :
            break
gugu(3)

###선생님이한
@gugu_deco
def gugu(dan):
    for i in range(1,10):
        print("%d * % d = %d"%(dan, i, dan*i))
gugu(3)













