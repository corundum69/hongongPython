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

