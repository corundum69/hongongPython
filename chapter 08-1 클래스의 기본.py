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