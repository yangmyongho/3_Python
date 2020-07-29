'''
패키지(package) = 폴더와 유사함
 - 유사한 모듈 파일을 저장하는 공간
모듈(module) = 파일과 유사함
 - 파이썬 파일(*.py)
클래스, 함수
 - 모듈에 포함되는 단위
'''


# from ..패키지명.모듈명 import 클래스 or 함수
from package_test.module01 import Sub
from package_test.module01 import Adder

sub = Sub(10,20) # 생성자 -> 객체
print('sub =', sub.calc()) # sub = -10

print('add =', Adder(10,30)) # add = 40  <함수 호출>





































