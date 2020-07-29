'''
 문) 동적 멤버 변수 생성으로 다음과 같은 산포도를 구하는 클래스를 정의하시오.
 
class Scattering :         
        
        생성자 
        
        분산 함수(var_func)
        var = sum((x - mean)**2) / (n-1)
        표준편차 함수(std_func) 
        std = sqrt(var)
        
   << 출력 결과 >>
 분산 : 7.466666666666666
 표준편차 :  2.7325202042558927
'''

from statistics import mean
from math import sqrt


class Scattering :
    def __init__(self, x):
        self.x = x

    def var_func(self):
        X = [(i - mean(self.x))**2 for i in self.x]
        self.var = (sum(X) / (len(self.x)-1))
    def std_func(self):
        self.std = sqrt(self.var)
    def final(self):
        print('분산 : %f \n' '표준편차 : %f'%(self.var, self.std))

x = [5, 9, 1, 7, 4, 6]
scattering = Scattering(x)
print(scattering.x) # [5, 9, 1, 7, 4, 6]
scattering.var_func()
print(scattering.var)
scattering.std_func()
print(scattering.std)

scattering.final()
