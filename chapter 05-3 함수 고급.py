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
## 함수의 매개변수로 함수 전달하기 (func_as_param.py
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)

## map() 함수와 filter() 함수 (call_with_func.py)
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
