# 리스트는 인덱스 기반으로 값을 저장하는 것이라면,
# 딕셔너리는 키를 기반으로 값을 저장하는 것이다

# 딕셔너리 선언하기
dict_a = {
    "name": "어밴저스 엔드게임",
    "type": "히어로 무비" 
    }

# 딕셔너리의 요소에 접근하기
dict_a
dict_a["name"]
dict_a["type"]

dict_b = {
    "director": ["안소니 루소", "조 루소"],
    "cast": ["아이언맨", "타노스", "토르", "닥터스트레인지", "헐크"] 
    }

dict_b
dict_b["director"]

## 딕셔너리의 요소에 접근하기 (dict01.py)
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색속"], # ingredient는 딕셔너리의 키이기도 하지만, 여러개의 자료를 가진 리스트이기도 하다
    "origin": "필리핀"
}

print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])

# 딕셔너리의 키의 특정값 출력
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색속"],
    "origin": "필리핀"
}
dictionary["ingredient"]
dictionary["ingredient"][1] # 키는 리스트이므로, 인덱스를 지정하여 특정값을 출력할 수 있다

# 딕셔너리의 문자열 키와 관련된 실수
dict_key = {
    name: "7D 건조 망고",
    type: "당절임"
}                # 오류

# 파이썬은 딕셔너리의 키에 단순한 식별자를 입력하면, 이를 변수로 인식하므로, name이란 이름으로 변수를 만들어 준다
# 하지만 이런 식의 코드를 사용하는 경우는 없으므로, 반드시 키를 문자열로 사용할 때는 반드시 따옴표를 붙인다
name = "이름"
dict_key = {
    name: "7D 건조 망고",
    type: "당절임"
}
dict_key

# 딕셔너리에 값 추가하기/제거하기
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색속"],
    "origin": "필리핀"
}
dictionary["price"] = 5000
dictionary

dictionary["name"] = "8D 건조 파인애플"
dictionary

del dictionary["ingredient"]
dictionary

## 딕셔너리에 요소 추가하기 (dict02.py)
dictionary = {}

print("요소 추가 이전:", dictionary)

dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"

print("요소 추가 이후:", dictionary)

## 딕셔너리에 요소 제거하기 (dict03.py)
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

print("요소 제거 이전:", dictionary)

del dictionary["name"]
del dictionary["type"]

print("요소 제거 이후:", dictionary)

# KeyError 예외
dictionary = {}
dictionary["key"]
del dictionary["key"]

# 딕셔너리 내부에 키가 있는지 확인하기
# in 키워드
## 키가 존재하는지 확인하고, 값에 접근하기 (key_in.py)
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색속"],
    "origin": "필리핀"
}

key = input("> 접근하고자 하는 키: ")

if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

# get() 함수
## 키가 존재하는지 않을 때, None을 출력하는지 확인 (get01.py)
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색속"],
    "origin": "필리핀"
}

value = dictionary.get("존재하지 않는 키")
print("값:", value)

if value == None:
    print("존재하지 않는 키에 접근하고 있습니다.")

# for 반복문: 딕셔너리와 함께 사용하기
## for 반복문과 딕셔너리 (for_dict.py)
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색속"],
    "origin": "필리핀"
}

for key in dictionary:
    print(key, ":", dictionary[key])

### 01. 딕셔너리는 키를 기반으로 여러 자료를 저장하는 자료형이다.
### 02. 키는 딕셔너리 내부에서 값에 접근할 때 사용하는 것이다.
### 03. 값은 딕셔너리 내부에 있는 각각의 내용을 의미한다   