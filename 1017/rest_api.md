# http request methods
- 리소스에 대한 행위를 정의
- we also call them http verbs
- get, post, put, delete ... etc
## resource
- http 요청 대상을 말한다
## http request methods
1. get
   - 서버에 리소스 표현을 요청
   - 검색용 데이터
2. post
   - 데이터를 지정된 리소스에 제출(submit)
   - 상태 변경하는 데이터
3. put
   - 요청 주소 리소스를 변경
4. delete
   - 리소스 삭제 명령

## URI
- uniform resource identifier (통합 자원 식별자)
- web 에서 리소스를 가리키는 문자열(url은 하나의 종류)
- urn (이름형태의 식별자), url, 등등

## URL
- uniform resource locator (통합 자원 위치)
- 웹에서의 리소스 주소

### Scheme(or protocol)
- 리소스 요청에 사용되는 프로토콜
- 어떤 규약을 사용하는지 나타난다
### Authority
- :// 이후에 나온다
- domain과 port 두 부분으로 나뉘어진다
- Domain 
  - 요청중인 웹 서버 주소
  - 실제로는 ip주소를 사용하고 있다
  - domain name을 할당하는 것 = Domain Name Service
- Port
  - 리소스에 접근하는데 사용하는 문(gate)
  - 표준 포트는 http : 80 https : 443 이 있다
  - 다만, 일반적인 상황에선 생략 가능
  - mailto 와 같은 경우에는 생략 불가능
- Path
  - 선택 사항
  - 초기에는 실제 물리적 위치였지만
  - 요즘에는 추상화된 형태의 구조
- Parameters
  - 서버에 제공하는 추가적 데이터
  - & 기호로 구분되는 key-value
- Anchor
  - 다른 부분에 대한 앵커
  - '#' 이후의 컨텐츠
  - 해당 지점으로 이동할 수 있게 해준다

### URN
- 독립적인 이름 역할을 하는 리소스
- 자원이 어디에 있는지 상관없이 이름만으로 자원을 식별
- URL의 형태를 보완하기 위해서 고안
- 하지만, 보편화된 방법이 없어 url을 활용 중

# REST API
## API
- Application Programming Interface
- 어플과 프로그래밍으로 소통하는 방법
## Web API
- 위의 방법을 활용하여 이제 웹 브라우저를 위한 API를 활용할 수 있다
- 직접 개발 보다는 여러 API를 가져다 쓰면 빠르게 구현할 수 있다
- 현재 대부분 json형식으로 데이터를 응답
## REST
- Representational State Transfer
- api 서버를 개발하기 위한 설계 방법론
- 소프트웨어 아키텍쳐 디자인 제약 모음 이다
- 이 원리를 따르면 RESTful 하다고 할 수 있다
- 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법에 대해 서술되어 있다

### REST 주소 지정 방법
1. 식별 : URI
2. 행위 : HTTP Method
3. 표현 : Json으로 데이터를 제공

## JSON
- 자바스크립트 표기법을 따른 단순 문자열
- key-value형태의 구조이다

## Response JSON
- Front end Framework를 통해 clinet 에게 더욱 좋은 화면을 출력할 수 있다
- 이때 전송되는 데이터가 Json
- 더이상 Django는 template 부분을 담당하지 않게 된다
- Vue.js를 통해 담당할 것이다
- 따라서 오늘은 Django의 json출력 방법에 대해 더욱 단련할 것임


### 다양한 방법으로 json 데이터 응답해보기
#### HTML 응답
1. 단순 렌더링 이다
2. 여태 하였던 방식이다

#### jsonresponse를 활용
1. HTML 문서가 아니라 json 데이터로 응답
2. 객체로 변환하여 view함수에서 발송
3. JsonResponse()함수

#### Django Serializer 를 활용
1. HttpResponse()함수 활용
2. 이전에는 모든 필드를 하나하나 입력했지만, 이젠 필요 없다
```python

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
```
3. 이전과 다르게 column을 일일이 정의할 필요 없고 model이 간단하게 반환되게 된다
##### Serializtion
- 데이터 구조나 객체를 저장후 재구성할 수 있는 포맷으로 변환하는 과정
- json이 보편적이다
- 즉, 포장이다

#### Django Rest Framework (DRF)
- django 에서 restfulapi 를 쉽게 구현하도록 도와주는 open source
- 거의 반드시 활용하게 된다
- DRF 의 serializer는 modelform 과 거의 유사하게 작동
- settings에 app에 등록하고, library 설치 후 사용 가능

#### Single Model
- many option
  - 단일 객체 인스턴스 대신 querty set이나 serialize 하려면 many=True 로 설정해 주어야 한다

#### Article
##### 조회
- 4개의 method에 따라 각자의 기능을 구현할 수 있다
- 이경우 하나의 url에서 crud 를 한곳에서 처리 할 수 있게 된다
``` python
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
```
- 추가로 drf에서는 데코레이터 작성이 필수
- 단일 조회시, pk를 부여하면 된다

##### 생성
- 이제 위의 함수에 분기점을 설정
```python
def article_list(request):
    if request.method == "GET":
    ...
    elif reqeust.method="POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.201(자동완성 됨))
        return Response(serializer.data, status=status.400)
# 각자의 상태에 따라 반환해야 하는 status를 정해줘야 함
```
- 추가로 is_valid안에 raies_exception=True를 부여하면 아래의 외부 return 항목은 필요 없어진다
##### 삭제
- 의 경우는 단순히 개별 조회에서 delete method확인

##### 수정
- 수정은 serializer 안에 data=request.data를 추가해 준다
- 기존 데이터를 유지하기 위함
- 외에는 post와 동일하다
- return 에는 200을 반환하게 한다

#### Comment
- 이 경우에는 거의 위와 동일
##### read_only_field
- 외래키의 경우, 전송하는 시점에서는 유효성 검사에서 제외, 조회시에는 출력하도록 할 수 있다
- read_only_fields 에 추가하면 된다
- 즉, validation field가 선택될 수 있다
- 추가로 역참조 필드 작성시, read_only=True를 반드시 부여하여야 한다(override시)
  - 테이블에는 물리적으로 존재하지 않은 필드이므로 해당 모델 안에서 조작이 불가능하다

