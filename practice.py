'''print('풍선')
print("나비")
print("ㅋ"*8)

print(5>10)
print(5<10)
print(True)
print(False)
print(not True)

station = ["사당","신도림", "인천공항"]
print( station[0], "행 열차가 들어오고 있습니다")
print( station[1], "행 열차가 들어오고 있습니다")
print( station[2], "행 열차가 들어오고 있습니다")
'''
from random import *

day1 = randrange(4,28)
day2 = randrange(4,28)
day3 = randrange(4,28)
day4 = randrange(4,28)

offline=max(day1,day2,day3,day4)

print("오프라인 스터디 모임 날짜는 매월 ", offline,"일로 선정 되었습니다.")


# 주석주석주석
# 주석주석주석
# 주석주석주석
# \" \' : 문장내에서 따옴표
# print("저는 '나도코딩'입니다")
# print("저는 \"나도코딩\"입니다")

# # \\ : 문장 내에서 \
# print("\\Hello World\\")
# \r : 커서를 맨 앞으로 이동
# \b : 백스페이스 (한글자 삭제)

#Web = "http://naver.com"
Web = "https://www.bing.com/search?q=naver&cvid=e3ccd15ec8b540f9be08bd7d6c7db268&pglt=547&FORM=ANNTA1&PC=U531"
my_str=Web.replace("http://","" )
my_str=my_str[:my_str.index('.')] 
password = my_str[:3]+str(len(my_str))+str(my_str.count('e'))+'!' 

print("{}의 비밀번호는 {}입니다.".format(Web, password))

