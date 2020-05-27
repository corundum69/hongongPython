## 쉬운 모듈 만들기 (module_basic/main.py)
import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))