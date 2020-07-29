'''
우편번호 검색
[우편번호]tab[도/시]tab[구]tab[동]
135-806	서울	강남구	개포1동 경남아파트		1
[우편번호]tab[도/시]tab[구]tab[동]tab[세부주소]
135-807	서울	강남구	개포1동 우성3차아파트	(1∼6동)	2
'''
import os
print(os.getcwd()) # C:\ITWILL\3_Python-I\workspacek


# 1. 주소 읽기
file = open('./chap07_FileIO/data/zipcode.txt', mode='r', encoding='utf-8')
line = file.readline() # 첫번째 한줄만
print(line) # 한줄 전체
print(line.split('\t')) # 토큰 단위 자르기
file.close()


# 2. 주소 검색
try:
    dong = input('동을 입력하세요 :')
    file = open('./chap07_FileIO/data/zipcode.txt', mode='r', encoding='utf-8')
    line = file.readline() # 첫번째줄 한줄만
    while line : # null == break
        address = line.split(sep='\t') # 토큰 단위 자르기
        if address[3].startswith(dong) : # startswith : 접두어
            print('['+address[0]+']', address[1], address[2], address[3], address[4]) #
        line = file.readline() # 두번째 ~ 마지막 줄 주소 읽음
except Exception as e:
    print("예외발생 :", e)
finally:
    print('~~종료~~')

























































