# 혼공파 12강 동영상 강의
# https://youtu.be/0jTIe3yG5yE

# 주어.동사(목적어) 형태로 사용하는 객체지향언어의 함수
# 예) "{}".format(100)

# 문자열의 format() 함수
## format() 함수로 숫자를 문자열로 변환하기 (format_basic.py)
string_a = "{}".format(10)

print(string_a)
print(type(string_a))

## format() 함수의 다양한 형태 (format01.py)
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연번 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

# IndexError 예외
# "{} {}".format(1, 2, 3, 4, 5)
# "{} {} {}".format(1, 2)

# format() 함수의 다양한 기능
## 정수를 특정 칸에 출력하기 (format02.py)
output_a = "{:d}".format(52)
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)
print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)

## 기호 붙여 출력하기 (format03.py)
output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)
print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)

## 조합해 보기 (format04.py)
output_h = "{:+5d}".format(52)
output_i = "{:+5d}".format(-52)
output_j = "{:=+5d}".format(52)
output_k = "{:=+5d}".format(-52)
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52)
print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)

# 부동소수점 출력의 다양한 형태
## float 자료형 기본 (format05.py)
output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)
output_c = "{:+15f}".format(52.273)
output_d = "{:+015f}".format(52.273)
print(output_a)
print(output_b)
print(output_c)
print(output_d)

## 소수점 아래 자릿수 지정하기 (format06.py)
output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)
print(output_a)
print(output_b)
print(output_c)

## 의미없는 소수점 제거하기 (format07.py)
output_a = 52.0
output_b = "{:g}".format(output_a)
print(output_a)
print(output_b)

# 대소문자 바꾸기: upper()와 lower()
a = "Hello Python Programming"
a.upper()
a.lower()

# 문자열 양옆의 공백 제거하기: strip()
input_a = """
    안녕하세요
문자열의 함수를 알아봅니다
"""
print(input_a)
print(input_a.strip())

# 문자열의 구성 파악하기: isOO()
print("TrainA10".isalnum())
print("10".isdigit())

# 문자열 찾기: find()와 rfind()
output_a = "안녕안녕하세요".find("안녕")
print(output_a)

output_a = "안녕안녕하세요".rfind("안녕")
print(output_a)

# 문자열과 in 연산자
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")

# 문자열 자르기: split()
a = "10 20 30 40 50".split(" ")
print(a)

### 01. format() 함수를 이용하면 숫자의 문자열을 다양한 형태로 출력할 수 있다.
### 02. upper()와 lower() 함수는 문자열의 알파벳을 대문자로 혹은 소문자로 변경한다.
### 03. strip() 함수는 문자열 양 옆의 공백을 제거한다.
### 04. find() 함수는 문자열 내부에 특정 문자가 어디에 위치하는지 찾을 때 사용한다.
### 05. in 연산자는 문자열 내부에 어떤 문자열이 있는지 확인할 때 사용한다.
### 06. split() 함수는 문자열을 특정한 문자로 자를 때 사용한다.
