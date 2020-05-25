# 리스트 선언하고 요소에 접근하기
[1, 2, 3, 4]
["안", "녕", "하", "세", "요"]
[273, 32, 103, "문자열", True, False]

list_a = [273, 32, 103, "문자열", True, False]
list_a[0]
list_a[1]
list_a[2]
list_a[1:3]  #문자열 범위 연산자에서 봤듯이, 뒷숫자 바로 앞번째까지만 출력함

list_a[0] = "변경"
list_a

# 첫째, 대괄호 안에 음수를 넣어 뒤에서부터 요소를 선택할 수 있다
list_a = [273, 32, 103, "문자열", True, False]
list_a[-1]
list_a[-2]
list_a[-3]

# 둘째, 리스트 접근 연산자를 다음과 같이 이중으로 사용할 수 있다
list_a = [273, 32, 103, "문자열", True, False]
list_a[3]
list_a[3][0]

# 셋째, 리스트 안에 리스트를 사용할 수 있다
list_a = [[1, 2,3], [4, 5, 6], [7, 8, 9]]
list_a[1]
list_a[1][1]

# 리스트에서의 IndexError 예외
list_a = [273, 32, 103]
list_a[3] #오류

# 리스트 연산자: 연결(+), 반복(*), len()
## 리스트 연산자 (list01.py)
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("# 리스트")
print("list_a =", list_a)
print("list_b =", list_b)
print()

print("# 리스트 기본 연산자")
print("list_a + list_b =", list_a + list_b)
print("list_a * 3 =", list_a * 3)
print()

print("# 길이 구하기")
print("len(list_a) =", len(list_a))

# 리스트에 요소 추가하기: append, insert
## 리스트에 요소 추가하기 (list02.py)
list_a = [1, 2, 3]

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)

# 리스트 연결 연산자와 요소 추가의 차이
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a + list_b # 비파괴적
list_a
list_b

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b) # 파괴적
list_a
list_b

# 리스트에 요소 제거하기
## 인덱스로 제거하기: del, pop (list03.py)
list_a = [1, 2, 3, 4, 5, 6]
print("# 리스트의 요소 하나 제거하기")

del list_a[1]
print("del list_a[1]:", list_a)

list_a.pop(2)
print("pop(2):", list_a)

list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]
list_b

list_c = [0, 1, 2, 3, 4, 5, 6]
del list_c[:6]
list_c

list_d = [0, 1, 2, 3, 4, 5, 6]
del list_d[3:]
list_d

# 값으로 제거하기: remove
list_c = [1, 2, 1, 2]
list_c.remove(2) # 앞 쪽의 2만 제거된다. 리스트에 중복된 여러개의 값을 모두 없애려면 반복문과 조합해서 사용한다
list_c

# 모두 제거하기: clear --> 웹개발, 인공지능에서도 많이 사용된다
list_d = [0, 1, 2, 3, 4, 5]
list_d.clear()
list_d

# 리스트 내부에 있는지 확인하기: in/not in 연산자
list_a = [273, 32, 103, 57, 52]
273 in list_a
99 in list_a
100 in list_a
52 in list_a

list_a = [273, 32, 103, 57, 52]
273 not in list_a
99 not in list_a
100 not in list_a
52 not in list_a
not 273 in list_a

# for 반복문
# for 반복문: 리스트와 함께 사용하기
## for 반복문과 리스트 (for_list.py)
array = [273, 32, 103, 57, 52]

for element in array:
    print(element)

for  character in "안녕하세요":  # for 반복문은 문자열을 함께 사용할 수도 있다
    print("-", character)


### 01. 리스트(list)는 여러 가지 자료를 저장할 수 있는 자료형을 말한다.
### 02. 요소(element)는 리스트 내부에 있는 각각의 내용을 의미한다.
### 03. 인덱스(index)는 리스트 내부에서 값의 위치를 의미한다.
### 04. for 반복문은 특정 코드를 반복해서 실행할 때 사용하는 기본적인 구문이다 

