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

# try except else 구문
## try except else 구문을 사용할 때는 예외가 발생할 가능성이 있는 코드만 try 구문 내부에 넣고
## 나머지는 모두 else 구문으로 빼는 경우가 많다
## try except else 구문 (try_except_else.py)
try:
    number_input_a = int(input("정수 입력> "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

# finally 구문
## finally 구문 (try_except_else_finally.py)
try:
    number_input_a = int(input("정수 입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a) 
except:
    print("정수를 입력해달라고 했잖아요")  
else:
    print("예외가 발생하지 않았습니다.")  
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")

## try, except, finally 구문
## try + except 구문 조합
## try + except + else 구문 조합
## try + except + finally 구문 조합
## try + except + else + finally 구문 조합
## try + finally 구문 조합

## finally에 대한 오해
## 파일이 제대로 닫혔는지 확인하기 (file_closed01.py)
try:
    file = open("info.txt", "w")
    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

## 파일 처리 중간에 예외 발생 (file_closed02.py)
try:
    file = open("info.txt", "w")
    예외.발생해라()
    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

## finally 구문 사용해 파일 닫기 (file_closed03.py)
try:
    file = open("info.txt", "w")
    예외.발생해라()
except Exception as e:
    print(e)
finally:
    file.close()

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

## try except 구문 끝난 후 파일 닫기 (file_closed04.py)
try:
    file = open("info.txt", "w")
    예외.발생해라()
except Exception as e:
    print(e)

file.close()

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

## try 구문 내부에서 return 키워드를 사용하는 경우 (try_return01.py)
## try 구문 내부에 return 키워드가 있는 것이 포인트이다.
## try 구문 중간에 탈출해도 finally 구문은 무조건 실행된다.
def test():
    print("test() 함수의 첫줄입니다")
    try:
        print("try 구문이 실행되었습니다")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다")
    else:
        print("else 구문이 실행되었습니다")
    finally:        
        print("finally 구문이 실행되었습니다") 
    print("test()함수의 마지막 줄입니다.")

test()

## finally 키워드 활용 (try_return02.py)
def write_text_file(filename, text):
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()

write_text_file("test.txt", "안녕하세요")

## 반복문과 함께 사용하는 경우 (finally_loop.py)
print("프로그램이 시작되었습니다")

while True:
    try:
        print("try 구문이 실행되었습니다")
        break
        print("try 구문의 break 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다")
    finally:
        print("finallry 구문이 실행되었습니다")
    print("while 반복문의 마지막 줄입니다.")
print("프로그램이 종료되었습니다.")

### 01. 구문오류는 프로그램의 문법적인 오류로 프로그램이 실행조차 되지않게 만드는 오류이다
### 02. 예외(런타임 에러)는 프로그램 실행중에 발생하는 오류이다.
### 03. 기본 예외처리는 조건문 등을 사용해 예외를 처리하는 기본적인 방법이다
### 04. try except 구문은 예외처리에 특화된 구문이다