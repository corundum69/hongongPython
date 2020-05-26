# 튜플
tuple_test = (10, 20, 30)
tuple_test[0]
tuple_test[1]
tuple_test[2]

## 튜플은 내부 요소 변경이 불가능하다.
tuple_test[0] = 1 #오류

## 요소를 하나만 가지는 튜플
type([273])
type((273))
type((273, ))

# 괄호 없는 튜플
## 리스트와 튜플의 특이한 사용 (tuple_basic.py)
[a, b] = [10, 20]
(c, d) = (10, 20)

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

## 괄호가 필요없는 튜플 (tuple_use01.py)
tuple_test = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()

a, b, c = 10, 20, 30
print("# 괄호가 없는 튜플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c:", c)

## 변수의 값을 교환하는 튜플 (tuple_use02.py)
a, b = 10, 20

print("# 교환 전 값")
print("a:", a)
print("b:", b)
print()

a, b = b, a

print("# 교환 후 값")
print("a:", a)
print("b:", b)
print()

# 튜플과 함수
## 여러 개의 값 리턴하기 (tuple_return.py)
def test():
    return (10, 20)

a, b = test()

print("a:", a)
print("b:", b)

## 튜플을 리턴하는 함수
a, b = 97, 40
divmod(a, b)
x, y = divmod(a, b)
x
y

# 람다
## 함수의 매개변수로 함수 전달하기 (func_as_param.py)
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)

## map() 함수와 filter() 함수 (call_with_func.py) --> 함수를 매개변수로 전달하는 대표적인 표준함수들이다.
def power(item):
    return item * item

def under_3(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행결과")
print("map(power, list_input_a):", output_b)
print("map(power, list_input_a):", list(output_b))

# 람다의 개념: 간단한 함수를 쉽게 선언하는 방법
## (사용법) lambda 매개변수: 리턴값
## 람다 (lambda01.py)
power = lambda x: x * x
under_3 = lambda x: x < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))

## 인라인 람다 (lambda02.py)
list_input_a = [1, 2, 3, 4, 5]

output_a = map(lambda x: x * x, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(lambda x: x < 3, list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))

# 파일 처리
## 파일 열고 닫기 (file_open.py)
file = open("basic.txt", "w")
file.write("Hello Python Programming")
file.close()

## with 키워드  --> 자동으로 파일이 닫힌다
## (사용법) with open(문자열: 파일경로, 문자열: 모드) as 파일객체:
##              문장
with open("basic.txt", "w") as file:
    file.write("Hello Python Programming")

## 프로그램이 외부 파일, 외부 네크워크 등과 통신할 때는 데이터가 흐르는 길을 만들어야 하는데, 이를 스트림이라 한다
## open() 함수는 프로그램에서 파일로 흐르는 길을 만드는 것이고, close() 함수는 프로그램에서 파일로 흐르는 길을 닫는 것이다.
## with 키워드는 이러한 스트림을 열고 닫는 실수를 줄이고자 만들어진 구문이며, 파일 및 네트워크 길을 열고 닫을 때 사용한다.

## 텍스트 읽기
## (사용법) 파일 객체.read()
## read() 함수로 텍스트 읽기 (file_read.py)
with open("basic.txt", "r") as file:
    contents = file.read()
print(contents)

## 텍스트 한 줄씩 읽기
## 텍스트를 사용해 데이터를 구조적으로 표현할 수 있는 방법은 csv, xml, json 등이 있다
## csv 파일은 한줄에 하나의 데이터를 나타내며, 각각의 줄은 쉼표를 사용해 데이터를 구분한다.
## 첫번째 줄에 헤더를 넣어 각 데이터가 무엇을 나타내는지 설명할 수 있다.
## 램덤하게 1000명의 키와 몸무게 만들기 (file_write.py)
import random

hanguls = list("가나다라마바사아자차카타파하")
with open("info.txt", "w", encoding='euc_kr') as file:  # encoding='euc_kr' 추가하면, 한글 안 깨진다
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))

# 반복문으로 파일 한 줄씩 읽기 (file_readlines.py)
with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(", ")

        if (not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / ((int(height) /100) **2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else: 
            result = "저체중"

        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()
        
# 제너레이터
## 제너레이터는 이터레이터를 직접 만들때 사용하는 코드이다.
## 함수 내부에 yield 키워드를 사용하면 해당 함수는 제너레이터 함수가 된다
## 일반 함수와 달리 함수를 호출해도 함수 내부의 코드가 실행되지 않는다
## 대신 함수의 리턴값으로 제너레이터를 리턴한다
## 제너레이터 객체는 next() 함수는 사용해 함수 내부의 코드를 실행하며,
## 이때 yield 키워드 부분까지만 실행하며, next() 함수의 리턴값으로 yield 키워드 뒤에 값만 출력한다 
## 이처럼 제너레이터 객체는 함수의 코드를 조금씩 실행할 때 사용한다
## 제너레이터 함수 (generator.py)
def test():
    print("함수가 호출되었습니다")
    yield "test"

print("A 지점 통과")
test()

print("B 지점 통과")
test()
print(test())

## 제너레이터 객체와 next() 함수
def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")

output = test()

print("D 지점 통과")
a = next(output)
print(a)

print("E 지점 통과")
b = next(output)
print(b)

print("F 지점 통과")
c = next(output)
print(c)

next(output)

### 01. 튜플은 리스트와 비슷하지만, 요소를 수정할 수 없는 파이썬의 특별한 문법이다. 괄호를 생략해서 다양하게 활용 가능하다
### 02. 람다는 함수를 짧게 쓸 수 있는 파이썬의 특별한 문법이다
### 03. with 구문은 블록을 벗어날 때 close() 함수를 자동으로 호출해 주는 구문이다