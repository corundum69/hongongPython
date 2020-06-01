# 객체
## 딕셔너리로 객체 만들기 (object_1_basic.py)
students = [
    {"name": "윤인성", "korean": 87, "math": 98, "english":88, "science":95},
    {"name": "연하진", "korean": 92, "math": 98, "english":96, "science":98},
    {"name": "구지연", "korean": 76, "math": 96, "english":94, "science":90},
    {"name": "나선주", "korean": 98, "math": 92, "english":96, "science":92},
    {"name": "윤아린", "korean": 95, "math": 98, "english":98, "science":98},
    {"name": "윤명월", "korean": 64, "math": 88, "english":92, "science":92},      
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")

## 객체를 만드는 함수(1) (object_2_dict.py)
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math, 
        "english": english,
        "science": science
    }

students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")

## 객체를 만드는 함수(2) (object_3_seperate.py)
## 객체와 관련된 코드를 분리할 수 있게 하는 것이 객체지향 프로그램의 핵심이다
## 아래 코드도 일종의 객체 지향 프로그래밍인데, 이런 코드가 너무 자주 사용되어 개발자들은 클래스라는 구조를 만들었다
## 클래스는 아래와 같은 형태의 코드를 조금 더 효율적으로 만들기 위한 기능이라고 생각하면 된다
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math, 
        "english": english,
        "science": science
    }

def student_get_sum(student):
    return student["korean"] + student["math"] +\
        student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student))

students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))

# 클래스 선언하기
## 클래스는 객체를 조금 더 효율적으로 생성하기 위해서 만들어진 구문이다.
## 클래스는 클래스 이름과 같은 함수(생성자)를 사용해 객체를 만든다
class Student:
    pass

student = Student()

students = [
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student()        
]

# 생성자
## 클래스 이름과 같은 함수를 생성자라고 한다
## 클래스 내부에 __init__라는 함수를 만들면 객체를 생성할 때 처리할 내용을 작성할 수 있다
## 클래스 내부의 함수는 첫번째 매개변수로 반드시 self를 입력해야 한다
## 이때 self는 '자기자신'을 나타내는 딕셔너리라고 생각하면 된다
## 다만, self가 가지고 있는 속성과 기능에 접근할 때의 self.<식별자> 형태로 접근한다

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math 
        self.english = english
        self.science = science

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

students[0].name
students[0].korean
students[0].math
students[0].english
students[0].science

# 메소드
## 클래스가 가지고 있는 함수를 메소드라 한다
## 클래스 내부에 메소드를 만들 때, 생성자와 선언하는 방법이 같다
## 다만, 첫번째 매개변수로 self를 넣어야 한다
## 클래스 내부에 함수(메소드) 선언하기 (object_4_class.py)
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

    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
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
    print(student.to_string())

### 01. 객체는 속성을 가질 수 잇는 모든 것을 의미한다.
### 02. 객체지향프로그램 언어는 객체를 기반으로 프로그램을 만드는 프로그래밍 언어이다
### 03. 추상화는 복잡한 자료, 모듈, 시스템 등으로부터 핵심적인 개념 또는 기능을 간추려 내는 것을 의미한다
### 04. 클래스는 객체를 쉽고 편리하게 생성하기 위해 만들어진 구문이다
### 05. 인스턴스는 클래스 이름과 같은 인스턴스를 생성할 때 만드는 함수이다
### 06. 생성자는 클래스 이름과 같은 인스턴스를 생성할 때 만드는 함수이다
### 07. 메소드는 클래스가 가진 함수를 의미한다