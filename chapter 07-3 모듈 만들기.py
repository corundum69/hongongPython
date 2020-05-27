# 모듈 만들기
## 쉬운 모듈 만들기 (module_basic/test_module.py)
PI = 3.141592

def number_input():
    output = input("숫자 입력> ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * redius

def get_circle_area(radius):
    return PI * radius * radius

## 쉬운 모듈 만들기 (module_basic/main.py)
import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

# __name__ == "__main__"
## __name__ --> 프로그래밍 언어에서는 프로그램 진입점을 엔트리 포인트 또는 메인이라고 부른다
## 이런 엔트리 포인트 또는 메인 내부에서의 __name__은 "__main__"이다.

## 모듈의 __name__ --> 모듈 내부에서 __name__을 출력하면 모듈의 이름을 나타낸다
## 모듈 이름을 출력하는 모듈 만들기 (module_main/main.py)
import test_module

print("# 메인의 __name__ 출력하기")
print(__name__)
print()

## 모듈 이름을 출력하는 모듈 만들기 (module_main/test_module.py)
print('# 모듈의 __name__ 출력하기')
print(__name__)
print()

## __name__ 활용하기
## 모듈 활용하기 (module_example/test_module.py)
PI = 3.141592

def number_input():
    output = input("숫자 입력> ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * redius

def get_circle_area(radius):
    return PI * radius * radius

print("get_circumference(10):", get_circumference(10))
print("get_circle_area(10):", get_circle_area(10))

## 모듈 활용하기 (module_example/main.py)
import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

# 패키지
## 패키지 만들기
## __init__.py 파일 --> 패키지를 읽어 들일때, __init__.py를 가장 먼저 실행한다

## 인코딩과 디코딩
## 텍스트 데이터와 바이너리 데이터
## 인터넷의 이미지 저장하기

### 01. 엔트리 포인트는 파이썬 명령어를 사용해서 첫 진입 파일을 엔트리 포인트라고 부른다
### 02. __name__=="__main__"는 현재 파일이 엔트리 포인트인지 확인할 때 사용하는 코드이다
### 03. 패키지는 모듈이 모인 것을 말한다