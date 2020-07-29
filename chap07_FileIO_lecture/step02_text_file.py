''''
텍스트 파일 입출력
형식)
    open(file, mode='r', 'w', 'a', 'r+')
'''
import os # 파일 경로


# 1. text 파일 읽기 <mode = 'r' , mode 생략가능>
'''
경로 : 절대 경로  vs  상대 경로
file.read() : 전체 문서 한번에 읽기
file.readline() : 전체 문서에서 한줄 읽기
file.readlines() : 전체 문서를 줄단위 읽기
'''
# 1-1) 절대 경로
print('현재 경로 :', os.getcwd()) # 현재 경로 : C:\ITWILL\3_Python-I\workspacek
# file open : 절대 경로
file1 = open(os.getcwd()+'/chap07_FileIO/data/ftest.txt', mode='r')
print(file1.read()) # file 사용
file1.close() # file close
''' programming is fun
    ~~~
    computer is input output system '''

# 1-2) 상대경로
print('현재 경로 :', os.getcwd()) # 현재 경로 : C:\ITWILL\3_Python-I\workspacek
# file open : 상대 경로 ( . : 현재 디렉터리 , .. : 상위 디렉터리
file1 = open('./chap07_FileIO/data/ftest.txt')
print(file1.read()) # file 사용
file1.close() # file close
''' programming is fun
    ~~~
    computer is input output system '''

# 1-3) readline()
file2 = open('./chap07_FileIO/data/ftest.txt')
# 1-3-1) 한줄읽기
row = file2.readline()
print('row :', row)
file2.close()
''' row : programming is fun '''
# 1-3-2) 여러줄 반복읽기
file2 = open('./chap07_FileIO/data/ftest.txt')
for i in range(6):
    row = file2.readline()
    print('row'+str(i),':', row)
file2.close()
''' row0 : programming is fun
    ~~~
    row5 : computer is input output system '''

# 1-4) readlines()
file3 = open('./chap07_FileIO/data/ftest.txt')
# 1-4-1) <list형>
rows = file3.readlines() # list 반환
print('rows :', rows)
file3.close()
''' rows : ['programming is fun\n', ~~~ , 'computer is input output system'] '''
# 1-4-2) <쪼개서 읽기>
for row in rows : # list를 string으로 쪼개기
    for sent in row.split('\n'): # 줄바꿈 기준으로 쪼개기
        if sent : # 공백지우기
            print(sent)
''' programming is fun
    ~~~
    computer is input output system '''
# 1-4-3) <string.strip()>
for row in rows :
    print(row.strip()) # 문장 끝에오는 불용어(공백, \n 기타) 전부 제거>
''' programming is fun
    ~~~
    computer is input output system '''


# 2. text 파일 쓰기 <mode = 'w'>
file4 = open('./chap07_FileIO/data/ftest2.txt', mode='w')
print(file4.write("my first text~~"))
file4.close()
''' my first text~~ '''


# 3. text 파일 추가 <mode = 'a'>
file5 = open('./chap07_FileIO/data/ftest2.txt', mode='a')
print(file5.write("\nmy second text~~"))
file5.close()
''' my first text~~
    my second text~~ '''


# 4. text 파일 추가,수정,읽기
with open("./chap07_FileIO/data/ftext3.txt", mode='w', encoding='utf-8') as file6 :
    file6.write('파이썬 파일 작성 연습')
    file6.write('\n파이썬 파일 작성 연습 2')
with open('./chap07_FileIO/data/ftext3.txt', mode='r', encoding='utf-8') as file7:
    print(file7.read())













































































































