# 불 만들기: 비교 연산자
print(10 == 100)
print(10 != 100)
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)

print("가방" == "하마")
print("가방" != "하마")
print("가방" < "하마") # 가나다 순으로 크기를 정하면, 앞에 있는 것의 크기가 작다
print("가방" > "하마")

# 불 연산하기: 논리 연산자
print(not True)
print(not False)

# not 연산자 조합하기 (boolean.py)
x = 10
under_20 = x < 20
print("under_20:", under_20)
print("not under_20", not under_20)

# and 연산자와 or 연산자
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# 논리연산자의 활용
# if 조건문이란?
if True:
    print("True입니다.")
    print("정말 True입니다.")

if False:
    print("False입니다.")

## 조건문의 기본 사용 (condition.py)
number = input("정수 입력> ")
number = int(number)

if number > 0:
    print("양수입니다.")

if number < 0:
    print("음수입니다.")

if number == 0:
    print("0입니다.")

## 날짜/시간 활용하기 (date.py)
import datetime

now = datetime.datetime.now()

print(now.year, "년")
print(now.month, "달")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

## 날짜/시간을 한줄로 출력하기 (date01.py)
import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.day,
    now.month,
    now.hour,
    now.minute,
    now.second
))

## 온전/오후를 구분하는 프로그램 (date02.py)
import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print(" 현재 시각은 {}시로 오전입니다.".format(now.hour))
    
if now.hour >= 12:
    print(" 현재 시각은 {}시로 오후입니다.".format(now.hour))

# 컴퓨터의 조건
## 끝자리로 짝수와 홀수 구분 (condition03.py)
number = input("정수 입력> ")
number = int(number)

if number % 2 == 0:
    print("짝수입니다")

if number % 2 == 1:
    print("홀수입니다")

### 01. 불(boolena)은 파이썬의 기본 자료형으로 True와 False를 나타내는 값이다.
### 02. 비교 연산자는 숫자 또는 문자열에 적용하며, 대소를 비교하는 연산자이다.
### 03. 논리 연산자는 not, and, or 연산자가 있으며, 불을 만들 때 사용한다.
### 04. if 조건문은 조건에 따라 코드를 실행하거나 실행하지 않게 만들고 싶을 때 사용하는 구문이다.