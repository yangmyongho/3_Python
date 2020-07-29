'''
문제2) 서울 지역을 대상으로 '동' 이름만 추출하여 다음과 같이 출력하시오.
  단계1 : 'ooo동' 문자열 추출 : 예) '개포1동 경남아파트' -> '개포1동'
  단계2 : 중복되지 않은 전체 '동' 개수 출력 : list -> set -> list
  
  <출력 예시>  
서울시 전체 동 개수 =  797
'''

try :
    file = open("./chap07_FileIO/data/zipcode.txt", mode='r', encoding='utf-8')
    line = file.readline() # 첫줄 읽기
    dong = [] # 서울시 동 저장 list
    while line : # null == break
        address = line.split(sep='\t') # 토큰 단위 자르기
        if address[1].startswith('서울') : # startswith : 접두어
            home = address[3].split(sep=' ')
            dong.append(home[0])
        line = file.readline() # 두번째 ~ 마지막 줄 주소 읽음
    dong = list(set(dong))
    dong.sort(reverse=False)
    print('서울특별시 전체 동의 개수 :', len(dong))
    for i in range(len(dong)):
        if i == 0 :
            print('['+dong[i]+']', end=', ')
        elif i % 10 == 0:
            print('['+dong[i]+']', end='\n')
        elif i == 796:
            print('['+dong[i]+']', end='')
        else:
            print('['+dong[i]+']', end=', ')
    #A = [i+'\n' if i  else i for i in dong]
    #print(A)

except Exception as e :
    print('예외발생 :', e)
