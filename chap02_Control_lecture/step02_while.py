'''
제어문 : 반복문(while)

while 조건식 :
    실행문
    실행문
'''


# 카운터, 누적 변수
cnt = tot = 0 # 변수 초기화

while cnt < 5 :
    cnt += 1 # 카운터 변수
    tot += cnt # 누적 변수
    print(cnt, tot, end=" / ")
# 1 1 / 2 3 / 3 6 / 4 10 / 5 15 /

while cnt < 5 : # True -> Loop(명령문 집합) 실행
    pass # 아무것도 하지않는다.
    break

# ex1) 1 ~ 100 까지 합 출력하기
cnt = tot = 0
while cnt < 100 :
    cnt += 1
    tot +=  cnt
print("1~100까지 합 : %d"%(tot)) # 1~100까지 합 : 5050
print("1~100까지 합 :", tot)

# ex2) 1 ~ 100 까지 짝수 출력
cnt = 0
data = [] # 빈 list(짝수 저장)
while cnt < 100 :
    cnt += 1
    if cnt % 2 == 0 :
        data.append(cnt) # 짝수 값 추가
print("짝수 값 :", data)

# ex3) 1 ~ 100 사이에서 5의배수 이면서 3의배수가 아닌값만 append 하기
cnt = 0
data = []
while cnt < 100 :
    cnt += 1
    if cnt % 5 == 0 and cnt % 3 != 0 :
        data.append(cnt)
print("5의배수 이면서 3의배수가 아닌값 :", data)
# 5의배수 이면서 3의배수가 아닌값 : [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95, 100]

''' 무한 loop -> 종료 조건 
종료 조건 : 0이면 종료한다.'''
while True :
    num = int(input("숫자 입력 : "))
    if num == 0 :
        print("프로그램 종료")
        break # 탈출(exit) : 종료 조건
    print("num =", num)

# random : 난수 생성
import random # 난수 생성 모듈
help(random.random) # random() -> x in the interval [0, 1).
help(random.choice) # Choose a random element from a non-empty sequence.
help(random.randint) # Return random integer in range [a, b], including both end points.
r = random.randint(1,5) # 모듈.함수 (1~5 난수)
print(r)
r = random.random() # 모듈.함수(0~1 난수)
print('r =', r)
'''r = 0.7022488599032701
   r = 0.9936632464625869
   r = 0.3603851296759477'''

# ex4) 난수 0.01미만이면 프로그램 종료, 아니면 난수 개수 출력
cnt = 0
while True :
    r = random.random()
    cnt += 1
    if r < 0.01 :
        print("프로그램 종료")
        break
print("난수 갯수 :", cnt, "개 \n r :", r)
'''프로그램 종료
난수 갯수 : 36 개
 r : 0.009539250499327023
프로그램 종료
난수 갯수 : 178 개
 r : 0.006572568922237676  '''
# 똑같음
cnt = 0
while True :
    r = random.random()
    if r < 0.01 :
        print("프로그램 종료")
        break
    else :
        cnt += 1
print("난수 갯수 :", cnt, "개")
'''프로그램 종료
난수 갯수 : 176 개'''


# 게임 만들어보기
print(">>> 숫자 맞추기 게임 <<<")
'''
숫자 범위 : 1 ~ 10
myInput == computer : 성공(exit) -> 종료 조건 
myInput > computer : '더 작은 수 입력'
myInput < computer : ' 더 큰 수 입력'
'''
computer = random.randint(1,10)
while True :
    myInput = int(input("예상 숫자 입력 : ")) # 사용자 입력
    if myInput == computer  :
        print('~~성공~~')
        break
    elif myInput > computer :
        print('~~더 작은 수 입력~~')
    else :
        print('~~더 큰 수 입력~~')
'''예상 숫자 입력 : >? 5
~~더 작은 수 입력~~
예상 숫자 입력 : >? 4
~~더 작은 수 입력~~
예상 숫자 입력 : >? 2
~~성공~~'''


'''
continue  vs  break
 - 반복문에서 사용되는 명령어
 - continue : 반복을 지속
 - break : 반복을 멈춤
'''
i = 0
while i < 10 :
    i += 1
    if i == 3 or i == 6 :
        continue # 다음 문장으로 skip
    if i == 9 :
        break
    print(i, end=' , ')
# 1 , 2 , 4 , 5 , 7 , 8 ,





