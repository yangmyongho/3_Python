'''
JSON 파일
 - 네트워크에서 표준으로 사용되는 파일 형식
 - 파일형식 : {key:value, key:value}, {key:value, key:value}
 - 활용 예 : 서로 다른 플랫폼(java, python)에서 파일 공유

 - json 모듈
    1. encoding(file save) : python object(list, dict) -> json file
    2. decoding(file read) : json file -> python object
'''
import os
print(os.getcwd()) # C:\ITWILL\3_Python-I\workspacek
import json
import pandas as pd


# 1. JSON 파일
# 1-1) python object
user = {'id' : 1234, 'name' : '홍길동'} # dict
print(user) # {'id': 1234, 'name': '홍길동'}  <python object>
print(type(user)) # <class 'dict'>

# 1-2) encoding : object -> 문자열
''' python object -> json 문자열 -> file save
     형식) json.dumps(object)  '''
json_str = json.dumps(user, ensure_ascii=False) # unicode -> asciicode(인코딩 안함)
print(json_str) # {"id": 1234, "name": "홍길동"}   <json 문자열>
print(type(json_str)) # <class 'str'>

# 1-3) decoding : 문자열 -> object
''' json 문자열 -> python object -> file read
     형식) json.loads(json 문자열)  '''
py_obj = json.loads(json_str)
print(py_obj) # {'id': 1234, 'name': '홍길동'}  <python object>
print(type(py_obj)) # <class 'dict'>


# 2. json file read/write
# 2-1) json file read : decoding
file = open('./chap07_fileIO/data/usagov_bitly.txt', mode='r', encoding='utf-8')
data = file.readlines() # 전체 내용 -> 줄단위 읽기
# decoding : json 문자열 -> python object
rows = [json.loads(row) for row in data]
print(len(rows)) # 3560
for row in rows[:10] :
    print(row)
    print(type(row))
# json object -> DataFrame
rows_df = pd.DataFrame(rows)
print(rows_df.info())
''' <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3560 entries, 0 to 3559
    Data columns (total 18 columns):  '''
print(rows_df.head())
print(rows_df.tail())

# 2-2) json file write : encoding
file = open('./chap07_fileIO/data/json_text.txt', mode='w', encoding='utf-8')
print(type(rows)) # <class 'list'> python object
for row in rows[:100]: # row = {key,value, ... } : dict
    json_str = json.dumps(row) # dict -> json 문자열
    file.write(json_str) # file save
    file.write('\n') # 줄바꿈 을 하지않으면 한줄에 계속저장이라서 계속 업데이트됌
print('file 저장 완료 ~~~')

# 2-3) json file read : decoding
file = open('./chap07_fileIO/data/json_text.txt', mode='r', encoding='utf-8')
data = file.readlines()
print(len(data)) # 100
# json decoding
rows = [json.loads(row) for row in data] # json 문자열 -> python object
rows_df = pd.DataFrame(rows)
print(rows_df.info())
''' <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 100 entries, 0 to 99
    Data columns (total 18 columns):  '''




































