'''
기본(default) 생성자
 - 생성자를 생략하면 기본 생성자가 만들어진다.
 - 묵시적 생산자
 - 객체만 생성하는 역할
'''

# 1. 기본 생성자
class default_cost:
    # 생성자 생략 < 기본 생성자 >
    def __init__(self):
        pass

    def data(self, x, y):
        self.x = x
        self.y = y
    def mul(self):
        re = self.x * self.y
        return re

obj = default_cost() # 기본 생성자
obj.data(10, 20) # data 생성 <10 20 을넣은걸 저장한다.>
print(obj.mul()) # 200

# 내가한 테스트
obj2 = default_cost()
# obj2.mul() 오류
# obj2.mul(10, 5) 오류
obj2.data(10, 5)
obj2.mul() # 50
# obj2.mul(5, 20) 오류


# 2. TV class 정의
class TV : # class = 변수(명사,자료) + 메서드(동사,자료처리)
    # 멤버변수 : 자료저장
    channel = volume = 0
    power = False # off(False) -> on(True)
    color = None # null

    # 기본 생성자
    def __init__(self):
        pass

    # 멤버메서드 < 볼륨, 채널, 전원>
    def volumeUp(self):
        self.volume += 1
    def volumeDown(self):
        self.volume -= 1
    def channelUp(self):
        self.channel += 1
    def channelDown(self):
        self.channel -= 1
    def changePower(self):
        self.power = not(self.power) # not = 반전(T -> F , F -> T)

    # 멤버변수 초기화 메서드 < 전역정보 초기화 >
    def data(self, channel, volume, color):
        self.channel = channel
        self.volume = volume
        self.color = color

    # TV 정보출력 메서드
    def display(self):
        print('전원 : {}, 채널 : {}, 볼륨 : {} , 색상 : {}'
              .format(self.power, self.channel, self.volume, self.color))

tv1 = TV()
tv1.display() # 전원 : False, 채널 : 0, 볼륨 : 0 , 색상 : None
tv1.data(5, 10, '검정색') # 전원 : False, 채널 : 5, 볼륨 : 10 , 색상 : 검정색
tv1.changePower() # off -> on
tv1.channelUp() # 5 -> 6
tv1.volumeDown() # 10 -> 9
tv1.display() # 전원 : True, 채널 : 6, 볼륨 : 9 , 색상 : 검정색


''' 
문 ) tv2 객체를 다음과 같이 생성하시오.
    단계1) 전원 : False, 채널 : 1, 볼륨 : 1, 색상 : 파란색 
    단계2) 전원 : True, 채널 : 10, 볼륨 : 15
    단계3) tv2 객체 정보 출력
'''
tv2 = TV()
tv2.display() # 전원 : False, 채널 : 0, 볼륨 : 0 , 색상 : None
tv2.data(1, 1, '파란색')
tv2.display() # 전원 : False, 채널 : 1, 볼륨 : 1 , 색상 : 파란색
tv2.changePower()
for i in range(9):
    tv2.channelUp()
for i in range(14):
    tv2.volumeUp()
tv2.display() # 전원 : True, 채널 : 10, 볼륨 : 15 , 색상 : 파란색


# 3. TV2 class
''' 기본 생성자를 생략하지않았을때'''
class TV2 : # class = 변수(명사,자료) + 메서드(동사,자료처리)
    # 멤버변수 : 자료저장
    channel = volume = 0
    power = False # off(False) -> on(True)
    color = None # null

    # 기본 생성자
    def __init__(self, channel, volume, color):
        self.channel = channel
        self.volume = volume
        self.color = color

    # 멤버메서드 < 볼륨, 채널, 전원>
    def volumeUp(self):
        self.volume += 1
    def volumeDown(self):
        self.volume -= 1
    def channelUp(self):
        self.channel += 1
    def channelDown(self):
        self.channel -= 1
    def changePower(self):
        self.power = not(self.power) # not = 반전(T -> F , F -> T)

    # 멤버변수 초기화 메서드 < 전역정보 초기화 >
    def data(self, channel, volume, color):
        self.channel = channel
        self.volume = volume
        self.color = color

    # TV 정보출력 메서드
    def display(self):
        print('전원 : {}, 채널 : {}, 볼륨 : {} , 색상 : {}'
              .format(self.power, self.channel, self.volume, self.color))

tv3 = TV2(1,1,'파란색')
tv3.display() # 전원 : False, 채널 : 1, 볼륨 : 1 , 색상 : 파란색








































