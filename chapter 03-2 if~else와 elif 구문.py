# else 조건문의 활용
## if 조건문에 else 구분을 추가하여 짝수 홀수 구분 (condtion04.py)
number = input("정수 입력> ")
number = int(number)

if number % 2 == 0:
    print("짝수입니다")

else:
    print("홀수입니다")

# elif 구문
## 계절 구하기 (condtion05.py)
import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("현재는 봄입니다.")
elif 6 <= month <= 8:
    print("현재는 여름입니다.")
elif 9 <= month <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")

## False로 변환되는 값 (false_value.py)
print(# if 조건문에 0 넣기")
if 0:
    print("0은 True로 변환됩니다.")
else:
    print("0은 False로 변환됩니다.")
print()

print(# if 조건문에 빈 문자열 넣기")
if "":
    print("빈문자열은 True로 변환됩니다.")
else:
    print("빈문자열은 False로 변환됩니다.")

# pass 키워드
number = input("정수 입력> ")
number = int(number)

if number > 0:
    pass
else:
    pass

# raise NotImplementError 키워드
number = input("정수 입력> ")
number = int(number)

if number > 0:
    raise NotImplementedError
else:
    raise NotImplementedError

### 01. else 구문은 if 조건문 뒤에 사용하며, if 조건문의 조건이 거짓일 때 실행된다.
### 02. elif 구문은 if 조건문과 else 조건문 사이에 입력하며, 세개 이상의 조건을 연결해서 사용할 때 적절하다.
### 03. if 조건문의 조건식에서 False로 변환되는 값은 none, 0, 0.0과 빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리 등이다.
### 04. pass 키워드는 프로그래밍의 전체 골격을 잡아 놓고, 내부에 처리할 내용은 나중에 만들고자할 때 pass라는 키워드를 입력해 둔다.