# 범위
# 첫째, 매개변수에 숫자를 한 개 넣는 방법
a = range(5)
a
list(range(10))
# 둘째, 매개변수에 숫자를 두 개 넣는 방법
list(range(0, 5))
list(range(5, 10))
# 셋째, 매개변수에 숫자를 세 개 넣는 방법
list(range(0, 10, 2))
list(range(0, 10, 3))

a = range(0, 10 + 1)
list(a)

# 수식에 나머지 연산자를 사용하는 경우
n = 10
a = range(0, n / 2) # flat 이므로 오류

a = range(0, int(n / 2)) # int 로 변환하여 오류 해결
list(a)

a = range(0, n // 2) # 하지만, 정수 나누기 연산자를 더 많이 씀
list(a)

# for 반복문: 범위와 함께 사용하기
## for 반복문과 볌위 (for_range.py)
for i in range(5):
    print(str(i) + "= 반복 변수")
print()

for i in range(5, 10):
    print(str(i) + "= 반복 변수")
print()

for i in range(0, 10, 3):
    print(str(i) + "= 반복 변수")
print()

# for 반복문: 리스트와 범위 조합하기
## 리스트와 범위를 조합해서 사용하기 (list_range01.py)
array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번째 반목: {}".format(i, array[i]))

# for 반복문: 반대로 반복하기
## 반대로 반복하기(1) (reversed_for01.py)
for i in range(4, 0 - 1, -1):
    print("현재 반복 변수: {}".format(i))

## 반대로 반복하기(2) (reversed_for02.py)
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))

# while 반복문
# while 반복문: for 반복문처럼 사용하기
## while 반복문을 for 반복문처럼 사용 (while_as_for.py)
i = 0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i += 1

# while 반복문: 상태를 기반으로 반복하기
## 해당하는 값 모두 제거하기 (while_with_condition.py)
list_test = [1, 2, 1, 2]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)

# while 반복문: 시간을 기반으로 반복하기
## 5초 동안 반복하기 (while_with_time.py)
## 이를 활용하면, 5초 동안 다른 사용자의 응답을 기다릴 수 있다. 통신할 때 자주 사용하는 코드이므로 시간을 기반으로 조건을 걸때 사용한다
import time

number = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("5초 동안 {}번 반복했습니다.".format(number))

# while 반복문: break 키워드/continue 키워드
# break 키워드는 무한 반복문을 만들고, 내부의 반목을 벗어날 때 많이 사용한다
## break 키워드 (break.py)
i = 0

while True:
    print("{}번째 반복문입니다.".format(i))
    i = i + 1

    input_text = input(">종료하시겠습니까?(y): ")
    if input_text in ["y", "Y"]:
        print("반복을 종료합니다")
        break

# continue 키워드는 현재 반복을 생략하고, 다음 반복으로 넘어갈 때 사용하는 키워드이다
## continue 키워드 (break01.py)
numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number < 10:
        continue
    print(number)

### 01. 범위는 정수의 범위를 나타내는 값이다. range()함수로 생성한다.
### 02. while 반복문은 조건식을 기반으로 특정 코드를 반복해서 실행할 때 사용하는 구문이다.
### 03. break 키워드는 반복문을 벗어날 때 사용하는 구문이다.
### 04. continue 키워드는 반복문의 현재 반복을 생략할 때 사용하는 구문이다.

