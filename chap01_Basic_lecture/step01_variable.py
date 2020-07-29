'''
변수 ( variable)
 - 형식) 변수명 = 값 or 수식 or 변수명
 - 자료를 저장하는 메모리 이름
 - type 선언 없음( R 과 동일)
'''

# 1. 변수와 자료
# 변수 자료형 확인
var1 = "Hello python"
var2 = 'Hello python'
print(var1) # line skip
print(var2) # <큰 따음표와 작은따음표 차이 없음>
print(type(var1),type(var2)) # <class 'str'> <class 'str'>

var1 = 100
print(var1,type(var1)) # 100 <class 'int'>

var3 = 150.25
print(var3,type(var3)) # 150.25 <class 'float'>

var4 = True
print(var4, type(var4)) # True <class 'bool'> 논리형


# 2. 변수명 작성규칙(p.11) <R과같은데 . 을 못쓴다>
_num10 = 10
_NUM10 = 20
# 대소문자 구분
print(_num10, _NUM10) # 10 20
print(id(_num10), id(_NUM10)) # 140737237319008 140737237319328

# 키워드 확인
import  keyword # 모듈 임포트 < lib에 있는 모듈 >
py_keyword = keyword.kwlist # 키워드 반환
print("파이썬 키워드 : ", py_keyword)
print("len =", len(py_keyword)) # len = 35

# 낙타체
korScore = 90 # 변수 = 상수
matScore = 85 # 변수 = 상수
engScore = 75 # 변수 = 상수
tot = korScore + matScore + engScore # 변수 = 수식
print("tot =", tot) # tot = 250


# 3. 참조변수 : 메모리 객체(value)를 참조하는 주소 저장 변수
x = 150 # 150 객체의 주소를 가지고있다.
x2 = 150 # 기존 객체가 있으면, 같은 주소를 반환한다.
y = 45.23 # 45.23 객체의 주소를 가지고있다.
y2 = y # 변수 복제(주소가 복제가 된다.)
# 변수 내용 출력
print(x, x2, y, y2) # 150 150 45.23 45.23
# 변수 주소 출력
print(id(x), id(x2), id(y), id(y2)) # 140737237323488 140737237323488 1526425433840 1526425433840