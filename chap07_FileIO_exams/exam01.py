#문제1) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오. 

'''
문단 내용 : split(sep='\n')
['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer']
문단 수 :  6

단어 내용 : split(sep=' ')
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer']
단어 수 :  22
'''
import os
print(os.getcwd()) # C:\ITWILL\3_Python-I\workspacek

try :
    file = open("./chap07_FileIO/data/ftest.txt", mode = 'r')
    rows = file.readlines()
    moon = []
    dan = []
    for row in rows:
        moon.append(row.strip())
        for sent in row.split(sep=' '):
            dan.append(sent.strip())
    print('문단 내용 :\n', moon, '\n문단 수 :', len(moon))
    print('단어 내용 :\n', dan, '\n단어 수 :', len(dan))
except Exception as e :
    print('예외발생 :', e)
finally:
    print('~~종료~~')
