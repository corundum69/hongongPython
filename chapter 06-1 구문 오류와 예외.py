# 오류의 종류
## 구문 오류: 실행 전에 발생하는 오류
## 예외: 실행 중에 발생하는 오류

# 기본 예외처리
## 예외를 처리하는 방법은 조건문을 사용하는 방법, try 구문을 사용하는 방법이 있다.

## 예외 상황 확인하기
## 조건문으로 예외 처리하기 (handle_with_condition.py)
user_input_a = input("정수 입력> ")

if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
else:
    print("정수를 입력하지 않았습니다.")

# try except 구문 (handle_with_try.py)
try:
    number_input_a = int(input("정수 입력> "))

    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("무언가 잘못되었습니다.")

# try except 구문과 pass 키워드 조합하기
## 숫자로 변환되는 것들만 리스트에 넣기 (try_pass.py)
list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_input_a))
print("{} 입니다.".format(list_number))


