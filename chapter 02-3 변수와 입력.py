# 혼공파 10~11강 동영상 강의
# https://youtu.be/KFYE6iRYBSY
# https://youtu.be/uPXZ2xEYAhc

# py 코드는 다른 이름의 파일로 저장하고, <ctrl> + F5 눌러 실행함

# 변수 만들기/사용하기
pi = 3.14159265
pi + 1
pi - 2
pi * 2
pi / 2
pi % 2
pi * pi

# 원의 둘레와 넓이 구하기
pi = 3.14159265
r = 10

print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2*pi*r)
print("원의 넓이 =", pi*pi*r)

# 복합 대입 연산자
number = 100
number += 10
number += 20
number += 30
print("number: ", number)

string = "안녕하세요"
string += "!"
string += "!"
print("string:", string)

# 사용자 입력: input()
## 입력 자료 확인하기 (input.py)
string = input("입력> ")

print("자료:", string)
print("자료형:", type(string))

## 입력받고 더하기 (input_error.py)
string = input("입력> ")

print("입력 + 100:", string + 100)

# 문자열을 숫자로 바꾸기
## int() 함수 활용하기 (int_convert.py)
string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("숫자 자료:", int_a + int_b)

## int()함수와 float()함수 활용하기 (int_float01.py)
output_a = int("52")
output_b = float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)

## int()함수와 float()함수 조합하기 (int_float02.py)
input_a = float(input("첫번째 숫자> "))
input_b = float(input("두번째 숫자> "))

print("덧셈 결과:", input_a + input_b)
print("뺄셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b)

#ValueError 예외
## 01. 숫자가 아닌 것을 숫자로 변환하려고 할 때
int("안녕하세요")
## 02. 소수점이 있는 숫자 형식의 문자열을 int()함수로 변환하려고 할 때
int("52.273")

#숫자를 문자열로 바꾸기
## str()함수를 사용해 숫자를 문자열로 변환하기 (str.py)
output_a = str(52)
output_b = str(52.273)

print(type(output_a), output_a)
print(type(output_b), output_b)

### 01. 변수 선언은 변수를 생성하는 것을 의미하고, 변수 할당은 변수에 값을 넣는 것을 의미한다.
### 02. 변수 참조는 변수에서 값을 꺼내는 것을 의미한다.
### 03. input() 함수는 명령 프롬프트에서 사용자로부터 데이터를 입력받을 때 사용한다.
### 04. int() 함수는 문자열을 int 자료형으로 변환하고, float() 함수는 문자열을 float 자료형으로 변환한다.
### 05. str() 함수는 숫자를 문자열로 변환한다.
