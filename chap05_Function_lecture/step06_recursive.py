'''
재귀호출(recursive call)
 - 함수 내에서 자신의 함수를 반복적으로 호출하는 기법
 - 반복적으로 변수의 값을 조정해서 연산 수행
 - 반드시 종료 조건이 필요하다.
 ex) 1 ~ n 누적의 합을 구하라
    (1 + 2 + 3 +...+ n)
'''


# 1. 카운터 : 1 ~ n
def Counter(n):
    if n == 0 : # 종료조건
        # print('프로그램 종료')
        return 0 # 함수 종료
    else :
        Counter(n-1) # 1. 재귀호출
        ''' 1. stack : [5(first), 4(5-1), 3(4-1), 2(3-1), 1(2-1)] 0(1-1)<stack에 저장되지않음>
            2. stack 역순으로 출력 <stack 특징 : 입력순서의 반대로 출력한다.>  '''
        print(n,end=' ') # 2. 카운트 : 1 2 3 4 5

Counter(5)
print()


# 2. 누적(1 + 2+ 3+ 4+ ...+ n)
def Adder(n):
    if n ==1 :
        return 1
    else:
        result = n + Adder(n-1) # 1. 재귀호출 -> 2. 누적 <Adder이라는 재귀호출부터 계속 반복하고 끝나면 그뒤에 더함>
        ''' stack : 후입선출 (LIFO)
            1. stack : [5(first), 4(5-1), 3(4-1), 2(3-1)] 1(2-1)<stack에 저장되지않음>
            2. stack 역순으로 누적 : 1+[2+3+4+5]    '''
        print(result, end=' ')
        return result

print(Adder(1)) # 1
print(Adder(5)) # 3 6 10 15 15















































































