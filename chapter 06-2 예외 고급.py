# 예외 객체
## 예외 객체 (except01.py)
try:
    number_input_a = int(input("정수 입력> "))
    
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)

# 예외 구분하기
## 여러가지 예외가 일어날 수 있는 코드 (except02.py)
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)

## 예외 구분하기 (except_multi.py)
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해 주세요")
except IndexError:
    print("리스트의 인덱스를 벗어났어요")

## 예외 구분 구문과 예외 객체 (except_as.py)
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해 주세요")
    print("exception:", exception)
except IndexError:
    print("리스트의 인덱스를 벗어났어요")
    print("exception:", exception)

# 모든 예외 잡기
## 예외 처리를 했지만 예외를 못 잡는 경우 (except03.py)
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()
except ValueError:
    print("정수를 입력해 주세요")
    print("exception:", exception)
except IndexError:
    print("리스트의 인덱스를 벗어났어요")
    print("exception:", exception)

## 모든 예외 잡기 (except_all.py)
## 마지막에는 모든 예외의 부모라고 할 수 있는 Exception을 넣어서 프로그램이 죽지 않게 하는 것이 좋다
## 큰 규모의 프로그램을 개발할 때는 '예외처리로 떡칠을 한다'라고 표현할 정도로 예외처리를 많이사용한다
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()
except ValueError:
    print("정수를 입력해 주세요")
    print("exception:", exception)
except IndexError:
    print("리스트의 인덱스를 벗어났어요")
    print("exception:", exception)
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)

# raise 구문
## 아직 구현되지 않는 부분에 일부로 예외를 발생시켜 프로그램을 죽게 만들어 잊어버리지 않도록 한다
## 이때 사용한 raise 키워드라 예외를 강제로 발생시키는 기능을 한다
number = input("정수 입력> ")
number = int(number)

if number > 0:
    raise NotImplementedError
else:
    raise NotImplementedError

# 다른 사람들이 작성한 코드를 살펴보는 것은 매우 도움이 된다
## Github의 Django 페이지 --> https://github.com/django/django
## Github에서 finally 검색하기 --> https://github.com/django/django/search?q=finally

### 01. 예외 객체는 예외와 관련된 정보를 담고 있는 객체이다.
### 02. raise 구문은 예외를 강제로 발생시킬 때 사용하는 구문이다.
### 03. Github 검색은 많은 사람들이 함께 개발하는 소셜코딩사이트 Gibhub를 이용하는 것으로 유능한 개발자들의 정제된 코드를 볼수 있다.  