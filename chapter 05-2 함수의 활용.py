# 재귀 함수
## 반복문으로 팩토리얼 구하기 (factorial_for.py)
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

## 재귀함수를 사용해 팩토리얼 구하기 (factorial_recursion.py)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

# 재귀 함수의 문제
## 재귀 함수로 구현한 피보나치 수열(1) (fibonacci_recursion01.py)
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n -2)

print("fibonacci(1):", fibonacci(1))
print("fibonacci(2):", fibonacci(2))
print("fibonacci(3):", fibonacci(3))
print("fibonacci(4):", fibonacci(4))
print("fibonacci(5):", fibonacci(5))

## 재귀 함수로 구현한 피보나치 수열(2) (fibonacci_recursion02.py)
counter = 0
def fibonacci(n):
    print("fibonacci({})를 구합니다.:".format(n))
    global counter
    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n -2)

fibonacci(10)
print("------")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))

## 메모화 (fibonacci_memo.py) --> 딕셔너리를 사용해서 한 번 계산한 값을 저장하는 것을 메모한다고 표현한다.
## 딕셔너리에 값이 메모되어 있으면, 처리를 수행하지 않고 곧바로 메모된 값을 돌려주면서, 코드의 속도를 빠르게 만든다.
## 메모화를 사용하면, 실행 후 곧바로 결과를 출력할 정도롤 속도가 빨라지며, 재귀함수와 함께 많이 사용되는 기술이다.
dictionary = {
    1: 1,
    2: 2
}
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output

print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))

# 조기 리턴
dictionary = {
    1: 1,
    2: 2
}
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]  # 흐름 중간에 return 키워드를 사용하는 것을 조기 리턴이라고 한다.
    output = fibonacci(n - 1) + fibonacci(n - 2)
    dictionary[n] = output
    return output

print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))

# 코드에 이름 붙이기
## 코드의 가독성을 높이려면 주석을 사용하며, 더 좋은 것은 함수를 만들어 사용하는 것이다.
## 한 줄 코드라도 의미를 가지고 있다면 함수로 만드는 것이 좋다
# 코드 유지보수
## 함수를 사용하면, 코드 수정을 함수 변경만으로 쉽게 할 수 있다.

### 01. 재귀함수는 내부에서 자기 자신을 호출하는 함수를 의미합니다.
### 02. 메모화는 한 번 계산한 값을 저장해 놓은 후, 이후에 다시 계산하지 않고 지정된 값을 활용하는 테크닉이다.
### 03. 조기 리턴은 함수의 흐름 중간에 return 키워드를 사용해서 코드 들여쓰기를 줄이는 등의 효과를 가져오는 테크닉이다.
