## 모듈 활용하기 (module_example/main.py)
import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))
