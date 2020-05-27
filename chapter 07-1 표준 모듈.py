# 모듈 사용의 기본: math 모듈
import math

math.sin(1)
math.cos(1)
math.tan(1)
math.floor(2.5)
math.ceil(2.5)

## 모듈 문서
## 표준 모듈 등의 정보가 궁금할 때, 가장 먼저 확인해야 하는 것이 파이썬 공식 문서이다.
## 파이썬 라이브러리 문서 --> https://docs.python.org/3/library/index.html

## from 구문
from math import sin, cos, tan, floor, ceil

sin(1)
cos(1)
tan(1)
floor(2.5)
ceil(2.5)

## as 구문
import math as m

m.sin(1)
m.cos(1)
m.tan(1)
m.floor(2.5)
m.ceil(2.5)

# random 모듈
## random 모듈 (module_random.py)
import random

print("# random 모듈")
print("- random():", random.random())
print("- uniform(10, 20):", random.uniform(10, 20))
print("- randrange(10):", random.randrange(10))
print("- choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))
print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))
print("- sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k=2))

## 파이썬 모듈은 사실 단순한 파이썬 파일이다. 따라서 모듈과 같은 이름으로 파일을 저장하지 않도록 주의한다

# sys 모듈
## sys 모듈 (module_sys.py)
import sys

print(sys.argv)
print("---")
print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

sys.exit()

# os 모듈
## os 모듈 (module_os.py)
import os

print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

os.mkdir("hello")
os.rmdir("heloo")

with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

os.remove("new.txt")
os.system("dir")

# datetime 모듈
## datetime 모듈 (module_datetime.py)
import datetime

print('# 현재 시각 출력하기')
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
    now.month,\
    now.day,\
    now.hour,\
    now.minute,\
    now.second)
output_c = now.strftime("%Y.%m.%d %H:%M:%S").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()

## 시간 처리하기 (module_datetime_add.py)
import datetime

now = datetime.datetime.now()

print("# datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(\
    weeks = 1,\
    days = 1,\
    hours = 1,\
    minutes = 1,\
    seconds = 1)

print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

# time 모듈
## time 모듈 (module_time.py)
import time

print("지금부터 5초 동안 정지합니다")
time.sleep(5)
print("프로그램을 종료합니다.")

# urllib 모듈
# urllib 모듈 (module_urllib.py)
from urllib import request

target = request.urlopen("https://google.com")
output = target.read()

print(output)

### 01. 표준모듈은 파이썬이 기본적으로 제공하는 모듈이다.
### 02. import 구문은 모듈을 읽어 들일 때 사용하는 구문이다.
### 03. as 키워드는 모듈을 읽어 들이고 별칭을 붙일 때 사용하는 구문이다.
### 04. 파이썬 문서는 모듈의 자세한 사용 방법이 들어있는 문서이다.