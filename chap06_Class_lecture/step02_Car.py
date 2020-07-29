'''
동적 멤버 변수 생성
 - 필요한 경우 특정 함수에서 멤버변수 생성
 self : 클래스의 멤버를 호출하는 역할
 self.멤버변수
 self.멤버메서드()
'''


class Car :
    # 멤버변수 <밑에서 명시해줘서 굳이 안해도됌>
    # door = cc = 0
    # name = None # null

    # 생성자 : 객체생성 + 변수값초기화
    def __init__(self, door, cc, name):
        # self.멤버변수 = 매개변수
        self.door = door # 동적멤버변수 생성
        self.cc = cc # 동적멤버변수 생성
        self.name = name # 동적멤버변수 생성

    # 멤버메서드 : 자료처리
    def info(self):
        self.kind = "" # 동적멤버변수 생성
        if self.cc >= 3000 : # 참조
            self.kind = "대형"
        else:
            self.kind = "소형"
        self.display()

    def display(self):
        print("%s는 %dcc(%s) 이고, 문짝은 %d개 이다."
              %(self.name, self.cc, self.kind, self.door))

# 객체1생성 : 생성자() -> object <car1.member or car1.member()>
car1 = Car(4, 2000, '소나타')
print('자동차 이름 :',car1.name) # 자동차 이름 : 소나타
car1.info() # 소나타는 2000cc(소형) 이고, 문짝은 4개 이다.

# 객체2생성
car2 = Car(2, 5000, '포르쉐')
print('자동차 이름 :',car2.name) # 자동차 이름 : 포르쉐
car2.info() # 포르쉐는 5000cc(대형) 이고, 문짝은 2개 이다.












