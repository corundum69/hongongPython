# 리스트에 적용할 수 있는 기본 함수: min(), max(), sum()
numbers = [103, 52, 273, 32, 77]
min(numbers) 
max(numbers) 
sum(numbers) 

min(103, 52, 273) 
max(103, 52, 273)

# reversed() 함수로 리스트 뒤집기
## reversed() 함수 (reversed.py)
list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 5]):", list_reversed)
print("list(reversed([1, 2, 3, 4, 5])):", list(list_reversed))
print()

print("# reversed() 함수와 반복문")
print("for i in reversed({1, 2, 3, 4, 5]):")
for i in reversed(list_a):
    print("-", i)

## reversed() 함수의 결과가 제너레이터이기 때문에 함수 결과를 여러 번 사용할 수 없는 일회용이다.
## 그러므로, for 구문 내부에 reversed() 함수를 곧바로 넣어서 사용한다
numbers = [1, 2, 3, 4, 5, 6]

for i in reversed(numbers):
    print("첫 번째 반복문: {}".format(i))

for i in reversed(numbers):
    print("두 번째 반복문: {}".format(i))

## 리스트 뒤집기 다른 방법: 확장 슬라이싱
numbers = [1, 2, 3, 4, 5]
numbers
numbers[::-1]

# enumerate() 함수와 반복문 조합하기
## 리스트의 요소를 반복할 때, 현재 인덱스가 몇 번째인지 확인해야 하는 경우가 많은데, 파이썬은 이런 코드를 위해 enumerate()를 제공한다
## 방법(1)
example_list = ["요소A", "요소B", "요소C"]
i = 0
for item in example_list:
    print("{}번째 요소는 {}입니다.".format(i, item))
    i += 1

## 방법(2)
example_list = ["요소A", "요소B", "요소C"]
for i in range(len(example_list)):
    print("{}번째 요소는 {}입니다.".format(i, example_list[i]))

## enumerate() 함수와 리스트 (enumerate.py)
example_list = ["요소A", "요소B", "요소C"]

print("# 단순 출력")
print(example_list)
print()

print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))

# 딕셔너리의 items() 함수와 반복문 조합하기
## 딕서너리의 items() 함수와 반복문 (items.py)
example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}

print("# 딕셔너리의 items() 함수")
print("items():", example_dictionary.items())
print()

print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))

# 리스트 내포
## 반복문을 사용한 리스트 생성 (for_list01.py)
array = []

for i in range(0, 20, 2):
    array.append(i * i)

print(array)

## 리스트 안에 for문 사용하기 (list_in.py)  --> 리스트내포(list comprehensions)
array = [i * i for i in range(0, 20, 2)]

print(array)

## 조건을 활용한 리스트 내포 (array_comprehensions.py)
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]  # array의 요소를 fruit이라고 할 때, 초콜릿이 아닌 fruit으로 리스트를 재조합하라는 의미
                                                         # array의 요소인 fruit들에 대해, 초콜릿이 없는 fruit들로 리스트를 다시 만들라는 의미
print(output)

# 구문 내부에 여러 줄 문자열을 사용했을 때의 문제점
## if 조건문과 여러 줄 문자열(1) (if_string.py)  --> 결과에서 원하지 않은 들여쓰기를 출력 
number = int(input("정수 입력> "))

if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는 짝수입니다.""".format(number, number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는 홀수입니다.""".format(number, number))

## 해결법 01. 괄호로 문자열 연결하기
## 여러 줄 문자열과 if구문을 조합했을 때의 문제해결(1) (string02.py)
number = int(input("정수 입력> "))

if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는 짝수입니다."
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는 홀수입니다."
    ).format(number, number))

## 해결법 02. 문자열의 join() 함수
## 여러 줄 문자열과 if구문을 조합했을 때의 문제해결(2) (string03.py)
number = int(input("정수 입력> "))

if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는 짝수입니다."
    ]).format(number, number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는 홀수입니다."
    ]).format(number, number))

# 이터레이터
## reversed() 함수와 이터레이터 (iterator01.py)
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)  # reversed() 함수의 리턴값이 바로 'reverseiterator'로 '이터레이터'이다

print("reversed_numbers :", r_num)
print(next(r_num))  # 이터레이터는 반복문의 매개변수로 전달할 수 있으며, next() 함수로 내부의 요소를 하나하나 꺼낼 수 있다
print(next(r_num))  # for 반복문의 매개변수에 넣으면 반복할 때마다 next()함수를 사용해 요소를 하나하나 꺼내준다
print(next(r_num))  # reversed() 함수는 리스트를 바로 리턴하지 않고, 이터레이터를 리턴해주는 이유는 메모리 절약을 위해서 이다
print(next(r_num))
print(next(r_num))

### 01. enumerate() 함수는 리스트를 매개변수로 넣을 경우, 인덱스와 값을 쌍으로 사용해 반복문을 돌릴 수 있게 해주는 함수이다.
### 02. items() 함수는 키와 쌍으로 사용해 반복문을 돌릴 수 있게 해주는 딕셔너리 함수이다.
### 03. 리스트 내포는 반복문과 조건문을 대괄호[] 안에 넣는 형태를 사용해서 리스트를 생성하는 파이썬의 특수 구문이다.