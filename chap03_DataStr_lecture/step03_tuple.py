'''
tuple 특징
 - index 사용, 순서 존재
 - 1차원 배열 구조
 - 수정 불가, 처리 속도 빠름
 - 제공 함수 없음 (추가, 삽입, 삭제) 불가능
 형식) 변수 = (원소1, 원소2, ...)
'''

tp = 10 # scala
tp1 = (10) # scala
print(tp, tp1, type(tp), type(tp1)) # 10 10 <class 'int'> <class 'int'>

# tuple 주의점 , 가 있어야 한다.
tp2 = (10, )
print(tp2, type(tp2)) # (10,) <class 'tuple'>

# index
tp3 = (10, 58, 4, 96, 55, 2)
print(tp3[:4]) # (10, 58, 4, 96)
print((tp3[-3:])) # (96, 55, 2)

# 수정 불가
# tp3[0] = 100 # type error

# max/min
vmax = vmin = tp3[0] # 첫번째 원소 -> 초기화
for t in tp3 : # (10, 58, 4, 96, 55, 2)
    if vmax < t :
        vmax = t
    if vmin > t :
        vmin = t
print('최댓값 =', vmax)
print('최솟값 =', vmin)
''' 최댓값 = 96
    최솟값 = 2 '''


# list -> tuple  < 변환하는이유 처리속도가 빨라서>
lst = list(range(1,10001))
print(lst)

tlst = tuple(lst)
print(type(tlst)) # <class 'tuple'>













