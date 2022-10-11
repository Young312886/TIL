# Static
## Managing Static files
- 업로드한 정적 파일을 클라이언트에게 제공한다
  
## Static files
- 정적 파일
- 별도의 조작없이 파일 내용을 그대로 보여주는 것
- 파일 자체가 고정되어 있게 된다
- 이미지, css, 등 추가 파일들
- 장고에서는 staticfiles라는 앱을 통해 관리하게 됨
  
### Media file
- 사용자가 웹에서 업로드 하는 모든 정적 파일(user-upload)
  
## Django 에 static files 구성 순서
1. Installed app 에 ststicfiles 가 있는가?
2. settings 에 ststic_url 정의
3. 앱의 static 폴더에, 정적파일 위치
4. 출력은, {% load static %} <'img src = {% static '경로' %}'> 로 url 파일에 작성

- load 태그
  - 라이브러리, 패키지에 등록된 것(태그와 필터)을 로드(input과 유사한 역할)
- static 태그
  - static_root에 저장된 정적파일에 연결

## Core Settings
1. STATIC_ROOT
   - Default : None
   - 정적 파일을 한곳에 모아두는 절대경로
   - 배포를 위해 수집하는 경로다
   - 개발 과정에선 적용되지 않는다
   - 배포 이후에는 cloud server를 통해 다른 서버가 실행하는 것이기 때문에, 내장된 정적 파일들을 밖으로 꺼내서 collect해 줘야 작동할 수 있다
2. SATICFILES_DIRS
   - app/static 외의 추가적인 정적 파일 경로들을 정의하는 리스트
3. STATIC_URL
   - root가 참조할때 사용할 url
   - 실제 파일이나 디텍토리가 아니며, url로만 존재하는 값이다

### Django 활용
- 아래 과정은 templates의 구성과 거의 동일하다(name_space 분리 과정 까지)
#### 기본 경로
1. App 폴더 안에 static 폴더 안에 app_name 폴더 안에 static file 추가

2. 아래의 형식 대로 url파일에 입력
```html
{ extends }
{load static}

<img src = "{% static 'articles/sample_img.png' %}>
``` 
#### 추가 경로
1. 가장 밖의 폴더에 static 폴더 구성
2. Staticfiles_dirs 루트 작성
3. 아래와 동일하게 작성
```html
{ extends }
{load static}

<img src = "{% static 'sample_img.png' %}>
```
- 두 방식의 차이점은 img의 url 구성에 차이점을 보인다는 것이다.

# Image
## Upload (미디어 파일)
- imagefield 를 활용하여 관리
### ImageField()
- 이미지 업로드에 사용
- filefield를 상속받는 서브 클래스
- 더하여 유효한 이미지인지 검사하는 기능이 포함되어 있음
- DB에는 최대 100자인 문자열로 들어가며, max_length가 먹힌다

### FileField()
- fielfield(upload_to = '', storage = None)
- 두개의 선택인자
- 활용하기 위해선
  1. media_root / media_url 을 settings에 설정
  2. upload_to 는 media_root의 하위 경로를 의미한다(선택)
#### media_root
- 성능을 위해 업로드 파일이 DB에 직접 저장되지 않음
- DB의 경로가 저장되게 된다
- 이경우, 저장된 디렉토리의 절대 경로가 바로 media_root
- 다만, static_root와는 반드시 다른 경로로 저장해야 한다
#### media_url
- 이 미디어 파일을 처리하는 url
  
### mediafile Django
1. settings에 media_url, media_root 입력
2. urls.py에 추가로 + static(settings.MEDIA_URL, document_root= setting.MEDIA_ROOT) 작성
3. 참고로 위의 과정은 장고 공식문서에 상세히 설명되어 있으니 참조!
4. model 에 imagefield 추가해 주고, model에도 적용
5. 추가로, form태그에 enctype 속성을 추가해 줘야 업로드 이후 작동하게 된다
6. views.py에도 추가로 request.post만이 아닌, request.files를 추가해 줘야 한다.(그림의 경우 post만으로 전달되지 않는다)

- 추가
- 업로드 디렉토리의 이름과 파일 이름 설정하는 방법 2가지
- upload_to안에 새로운 이미지 저장 경로를 추가(함수안에)
- 시간을 함수 경로 안에 포함시키는 방법 또한 유효하다
- 다른 방법이로는 함수를 호출하여 더 많은 정보를 저장하는 방식이다
- class밖에 upload_to에 저장할 경로를 return하는 함수를 정의해 준다
- instance의 username 과 filename을 포함시키는 방법 사용 가능

### Image Resizing
- 태그에서 직접 사이즈를 조정할 수 있지만, 용량 이슈는 여전히 존재
- 업로드시에 resizing하는 방법이 있다
- django-imagekit 라이브러리 활용
- processimagefield를 활용해서 upload되는 이미지의 크기, 화질을 미리 정의된 조건으로 받아들이게 된다

### 캐시
- 캐시의 경우 브라우저가 저장하고 있다가 호출되면 간단하게 호출하게 된다.


# QuerySet API Advanced
## sorting data
### .count()
- 현재 queryset의 개체 수를 세어서 준다
### .order_by('col')
- 순서 재정렬
- 앞에 -를 붙여주면 내림차순
- ? 는 랜덤 정렬
### .values()
- 원하는 field를 따로 출력시키도록 설정(빈칸이면 그냥 다)
- 딕셔너리 형태로 출력하게 된다

## filtering data
### .distinct()
- 중복없이 출력하는 방법

### field__lookup
- __두번을 연결해서 뒤에 조건을 상세히 설정해 줄 수 있다

### .exclude()

### [:n]
- 슬라이싱도 가능

### 조건이 여러개이면서 or인 경우
- from django.db.models import Q
- Q안에 조건을 담아서 | (=or) 을 달아주면 연산이 가능
- 반면, 의 경우는 and
- Q외에도 다양한 함수들이 포함되어 있다(더 강력한 조건 부여 가능)

### aggregate()
- 평균, 숫자, max, min 등을 출력 가능
- 딕셔너리 값으로 반환

### annotate()
- 각 컬럼에 대한 요약값을 붙여주는 것이다
- annotate(count('country'), aver = Avg('balance'))
- 형식으로 뒤에 계속해서 붙여줄 수 있다