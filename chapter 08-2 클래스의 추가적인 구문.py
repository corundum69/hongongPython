# 클래스를 사용하는 것은 작정하고 속성(변수)과 기능(함수)를 가진 객체를 만들겠다고 하는 것이다

# 어떤 클래스의 인스턴스인지 확인하기
## 객체(인스턴스)가 어떤 클래스로부터 확인할 수 있도록 isinstance() 함수를 제공한다
## isinstance() 함수는 첫번째 매개변수에 객체(인스턴스), 두번째 매개변수에 클래스를 입력한다
## 이때 인스턴스가 해당 클래스를 기반으로 만들어졌으면 True, 전혀 상관없는 인스턴스와 클래스라면 False를 리턴한다
class Student:
    def __init__(self):
        pass

student = Student()

print("isinstance(studnet, Student):", isinstance(student, Student))

## isinstance() 함수활용 (isinstance.py)
## 일반적으로 객체지향 프로그래밍은 모든 데이터를 클래스로 구현한다
## 이러한 데이터를 관리할 때 종류별로 클래스를 따로 만들어 사용해야 한다고 생각하는데,
## isinstance() 함수를 사용하면 리스트로부터 여러 종류의 데이터를 다룰 수 있다
class Student:
    def study(self):
        print("공부를 합니다")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다")

classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

# 특수한 이름의 메소드
## __str__() 함수 (str_func.py)
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math 
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))

## 크기 비교 함수 (compare_func.py)
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math 
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

student_a = Student("윤인성", 87, 98, 88, 95),
student_b = Student("연하진", 92, 98, 96, 98),

print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a > student_b = ", student_a > student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a < student_b = ", student_a < student_b)
print("student_a <= student_b = ", student_a <= student_b)

# 클래스 변수와 메소드
## 클래스 변수
## (만들기) class 클래스 이름:
##             클래스 변수 = 값
## (사용하기) 클래스 이름.변수이름
## 클래스 변수 (class_var.py)
class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math 
        self.english = english
        self.science = science

        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print()
print("현재 생성된 총 학생 수는 {}명 입니다.".format(Student.count))

## 클래스 함수
## 클래스 데코레이터
## @로 시작하는 것을 파이썬에서는 '데코레이터'라고 하며, '꾸며 주는 것'이라는 의미를 가진다
## (만들기) class 클래스 이름:
##             @classmethod
##             def 클래스 변수(cls, 매개변수):
##                 pass
## (사용하기) 클래스 이름.함수이름(매개변수)
## 클래스 변수 (class_func.py)
class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("------ 학생 목록 -----")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------ ----- -----")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math 
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)

Student.print()

## 가비지 컬렉터
## A가 생성되고, 다음 줄로 넘어갈 때, 이것을 변수에 저장하지 않으면,
## 가비지 컬렉터는 이후에 활용지 않겠다는 의미로 이해하고, 메모리를 아끼기 위해 과감히 지운다
## 가비지 컬렉터: 변수에 저장하지 않는 경우 (garbage01.py)
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))

Test("A")
Test("B")
Test("C")

## 가비지 컬렉터: 변수에 저장한 경우 (garbage02.py)
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))

a = Test("A")
b = Test("B")
c = Test("C")

## 프라이빗 변수와 게터/세터
## 객체 지향 프로그래밍의 최종 목표는 객체를 효율적으로 만들고 사용하는 것이다
## 원의 둘레와 넓이를 구하는 객체지향 프로그램 (math_sample.py)
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.radius
    def get_area(self):
        return math.pi * (self.radius ** 2)

circle = Circle(10)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

## 프라이빗 변수
## 파이썬은 클래스 내부의 변수를 외부에서 사용하는 것을 막고 싶을때 인스턴스 변수 이름을 __<변수이름> 형태로 선언한다
## 프라이빗 변수 (private.py)
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

print("# __radius에 접근합니다")
print(circle.__radius)

## 게터와 세터
## 게터와 세터는 프라이빗 변수의 값을 추출하거나 변경할 목적으로, 간접적으로 속성에 접근하도록 해주는 함수이다
## 게터와 세터 (getter_setter.py)
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value

circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

print("# __radius에 접근합니다")
print(circle.get_radius())
print()

circle.set_radius(2)
print("# 원의 둘레와 넓이를 구합니다")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

## 데코레이터를 사용한 게터와 세터
## 게터와 세터 사용이 많아져, 쉽게 만들수 있는 기능을 제공한다
## 데코레이터를 사용해 게터와 세터 만들기 (deco1.py)
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise TypeError("길이는 양의 숫자여야 합니다")
        self.__radius = value

print("# 데코레이터를 사용한 Getter와 Setter")
circle = Circle(10)
print("원래 원의 반지름: ", circle.radius)
circle.radius = 2
print("변경된 원의 반지름: ", circle.radius)
print()

print("# 강제로 예외를 발생시킵니다")
circle.radius = -10

# 상속
## 상속: 다른 누군가 만들어 놓은 기본 형태에 내가 원하는 것만 교체하는 것
## 다중상속: 다른 누군가 만들어 놓은 형태들을 조립해서 내가 원하는 것을 만드는 것
 
## 상속의 활용 (inherit01.py) 
## 아래 코드 전체가 상속하는 구문이므로, 상속을 활용하고자 한다면 모두 외어야 한다
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")

child = Child()
child.test()
print(child.value)

## 예외 클래스 만들기
## 사용자 정의 예외 클래스 만들기 (inherit02.py)
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)

raise CustomException

## 자식 클래스로써 부모의 함수 재정의(오버라이드)하기 (inherit03.py)
## 부모에 정의되어 있는 함수를 자식에서다시 정의하는 것을 재정의 또는 오버라이드라고 한다
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("#### 내가 만든 오류가 생성되었어요 ####")
        
    def __str__(self):
        return "오류가 발생했어요"

raise CustomException


## 자식 클래스로써 부모에 없는 새로운 함수 정의하기 (inherit04.py)
class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value
        
    def __str__(self):
        return self.message

    def print(self):
        print("#### 오류 정보 ####")
        print("메시지:", self.message)
        print("값:", self.value)

try:
    raise CustomException("딱히 이유 없음", 273)
except CustomException as e:
    e.print()

### 01. isinstance() 함수는 어떤 클래스의 인스턴스인지 확인할 때 사용하는 함수이다
### 02. 클래스 변수와 클래스 함수는 클래스 이름 뒤에 .(마침표)를 찍고 바로 사용할 수 있는 클래스가 갖고 있는 변수와 함수이다
### 03. 상속은 어떤 클래스를 기반으로 그 속성과 기능을 뮬려받아 새로운 클래스를 만드는 것을 말한다.