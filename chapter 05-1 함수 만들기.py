# 함수의 기본
## 기본적인 함수 (fun_basic.py)
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()

# 함수에 매개변수 만들기
## 매개변수의 기본 (param_basic.py)
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)

# 매개변수와 관련된 TypeError
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요")
print_n_times("안녕하세요", 10, 20)

# 가변 매개변수
## 가변 매개변수 뒤에는 일반매개변수가 올 수 없다.
## 가변 매개변수는 하나만 사용할 수 있다.
## 가변 매개변수 함수 (variable_param.py)
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

# 기본 매개변수
## 기본 매개변수 (default_param.py)
def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("안녕하세요")

# 키워드 매개변수
# 기본 매개변수가 가변 매개변수보다 앞에 올 때
def print_n_times(n=2, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍") # n에 "안녕하세요"가 들어가 오류

# 가변 매개변수가 기본 매개변수보다 앞에 올 때
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", 3) # 3까지 출력을 2번 진행

# 키워드 매개변수 --> 매개변수 이름을 지정해서 입력하는 매개변수
## 키워드 매개변수 (param_keyword01.py)
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)

# 기본 매개변수 중에서 필요한 값만 입력하기
## 일반적으로 '일반 매개변수'는 필수로 입력하며, 순서에 맞게 입력한다.
## '기본 매개변수'는 필요한 것만 키워드를 지정해서 입력하는 경우가 많다.
## 여러 함수 호출 형태 (param_examples.py)
def test(a, b=10, c=100):
    print(a + b + c)

test(10, 20, 30)
test(a=10, b=100, c=200)
test(c=10, a=100, b=200)
test(10, c=200)

# 리턴 --> 리턴 키워드를 만나는 순간 함수는 종류된다
## 자료없이 리턴하기 (return_only.py)
def return_test():
    print("A 위치입니다")
    return
    print("B 위치입니다")

return_test()

# 자료와 함께 리턴하기 (return_with_data.py)
def return_test():
    return 100

value = return_test()
print(value)

# 아무것도 리턴하지 않았을 때의 리턴값 (return_none.py)
def return_test():
    return

value = return_test()
print(value)

# 기본적인 함수의 활용
## 범위 내부의 정수를 모두 더하는 함수 (sum_all_basic.py)
def sum_all(start, end):
    output = 0
    for i in range(start, end +1):
        output += i
    return output

print("0 to 100:", sum_all(0, 100))
print("0 to 1000:", sum_all(0, 1000))
print("50 to 100:", sum_all(50, 100))
print("500 to 1000:", sum_all(500, 1000))

## 기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수 (sum_all_with_default.py)
def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end +1, step):
        output += i
    return output

print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))

## 함수를 어떻게 잘 만들 것인지는 사실 코드를 많이 보는 방법 밖에 없다.

### 01. 호출은 함수를 실행하는 행위를 말한다.
### 02. 매개변수는 함수의 괄호 내부에 넣는 것을 의미한다.
### 03. 리턴값은 함수의 최종적인 결과를 의미한다.
### 04. 가변 매개변수 함수는 매개변수를 원하는 만큼 받을 수 있는 함수이다.
### 05. 기본 매개변수는 매개변수에 아무것도 넣지 않아도 들어가는 값이다. 