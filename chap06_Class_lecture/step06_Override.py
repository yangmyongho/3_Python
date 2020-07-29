'''
1. 메서드 재정의(method override)
    - 부모의 원형 메서드 -> 자식에서 원형 메서드를 다시 작성하는 문법
    - 상속관계에서만 나오는 용어
    - 인수, 내용 -> 수정 대상
2. 다형성
    -상속관계에서만 나오는 용어
    - 한 가지 기능 -> 2개 이상 결과 생성( + -> 덧셈, 결합)
    - 부모 객체 -> (자식1, 자식2) 멤버 호출
'''


# 1. 메서드 재정의(method override)

'''부모 클래스'''
class Super :
    data = None # 멤버변수
    # 기본 생성자 : 객체만 생성
    # 멤버메서드 : 원형메서드
    def super_Func(self):
        pass # 내용없음

'''자식 클래스 1'''
class Sub1(Super):
    # data
    # def super_Func
    def super_Func(self, data): # 수정 -> override
        self.data = data
        print('자식1 : data = {}'.format(data))

sub1 = Sub1()
sub1.super_Func('20200414') # 자식1 : data = 20200414

'''자식 클래스 2'''
class Sub2(Super):
    # data
    # def super_Func
    def super_Func(self, data): # 수정 -> override
        self.data = data
        print('자식2 : data = {}'.format(data**2))

sub2 = Sub2()
sub2.super_Func(100) # 자식2 : data = 10000


# 2. 다형성
sup = Super() # 부모 객체
sub1 = Sub1() # 자식1 객체
sub2 = Sub2() # 자식2 객체

sup.super_Func() #
sup = sub1
sup.super_Func(15) # 자식1 : data = 15
sup = sub2
sup.super_Func(15) # 자식2 : data = 225









































































































































