# 모듈 설치하기
## (사용법) >pip install 모듈이름

# 모듈 찾아보기
## 1. 책을 샀는데 책에서 모듈을 추천해 주었다
## 2. 파이썬 커뮤니티에 가입했는데, 어떤 모듈이 어떤 분야에서 인기라고 한다
## 3. 어떤 기능이 있는 모듈이 필요해서 구글에서 검색해 보았다(python + 관심분야)

# BeautifulSoup 모듈
from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stdId=108")

soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()

# Flask 모듈
## Flask 모듈 사용하기 (flask_basic.py)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h>"

if __name__ == '__main__':
	app.run()

## BeautifulSoup 스크레이핑 실행하기 (beautiful_flask.py)
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route("/")

def hello():
    target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stdId=108")
    soup = BeautifulSoup(target, "html.parser")
    output = ""

    for location in soup.select("location"):
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}<br/>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}"\
            .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string\
            )
        output += "<hr/>"
    return output

if __name__ == '__main__':
	app.run()

# 라이브러리와 프레임워크
## 라이브러리: 개발자가 모듈의 기능을 호출하는 형태의 모듈
## 프레임워크: 모듈이 개발자가 작성한 코드를 실행하는 형태의 모듈

# 데코레이션
## @로 시작하는 구문을 파이썬에서는 데코레이션이라고 한다

# 함수 데코레이션의 기본
## 함수 데이코레이션의 기본 (func_deco.py)
def test(function):
    def wrapper():
        print("인사가 시작되었습니다")
        function()
        print("인사가 종료되었습니다")
    return wrapper

@test
def hello():
    print("hello")

hello()

### 01. 외부모듈은 파이썬이 기본적으로 제공하지 않는, 다른 사람들이 만들어 제공하는 모듈을 의미한다
### 02. pip install은 외부 모듈을 설치할 때 사용하는 명령어이다
### 03. 제어역전은 개발자가 모듈의 함수를 호출하는 것이 일반적인 제어흐름이나, 이와 반대로 개발자가 만든 함수를 모듈이 실행하는 것을 말한다
### 04. 라이브러리는 개발자가 모듈의 기능을 호출하는 형태와 같이 정상적인 제어를 하는 모듈이다
### 05. 프레임워크는 모듈이 개발자가 작성한 코드를 실행하는 형태의 모듈이다