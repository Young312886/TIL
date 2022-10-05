# Reltaionship of Database
## many-to-one relationship
- 외래 키 속성을 사용해 모델간 n:1 관계 설정
- 관계란?
  - 테이블간의 상호작용을 기반으로 참조, 논리적 연결이 이뤄진다
### Foreign Key
- 한 테이블의 필드 중 다른 테이블의 행을 식별하는 키
- 즉, 참조되는 측 테이블의 Primary key 값을 활용
- 그 값은 참조되는 테이블 하나 값에 대응
- 없는 값은 참조할 수 없다
- 참조하는 테이블의 여러 값이 하나의 값을 참조할 수 있다
- 이게 바로 N:1
- 부모 테이블(참조되는 테이블)의 유일값(참조 무결성)
- 기본키 일 필요는 없지만, 유일값을 가져야 한다
- 참조 무결성
  - 테이블 간의 일관성
  - 부모 테이블의 유일값을 사용해야 하는 이유
### N:1 relationship, in our project
- Comment - Article
### Django relationship fields
- OneToOneField()
- ForeignKey() : N-1
- ManyToManyField() : N-N

#### ForeignKey()
- 장고 모델에 어디에 작성하더라도 실제 테이블에서는 마지막 칼럼으로 들어가게 된다
- 칼럼 변수 설정시 모델 클래스 단수형으로 표현해주자
```python
aritcle = models.ForeignKey(Article, on_delete=models.CASCADE)
```
- to : 참조할 대상(클래스)
- on_delete : 옵션
- 위의 두개는 필수 인자이다
##### on_delete
- 참조하는 객체가 사라지면 처리 방법에 대한 정의
- 데이터 무결성을 유지해 주는 옵션
- CASCADE = 삭제되면 참조하는 객체도 삭제
- Protect, set_null, set_default 등등 다양

#### 관계 모델 참조
- 1에서 N을 참조하는 것은 역참조
- 이전과 같이 objects를 활용
```python
aritcle.comment_set.method()
```
- _set manager 라고 불림
- 이것을 통해  댓글 객체를 참조할 수 있다(자동참조)
- article 에 참조가 걸린 친구들을 article에서 역조회 가능
#### Django
- article을 받아오고 등록하고, content로 html에 보내는 과정은 동일
- 다만, article을 지정하고 comment를 작성하는 과정이 존재하고 있다
- ModelForm exclude 에 article 정보를 추가하여 출력하지 않도록 설정
- 다만, 위의 경우 view함수에서 pk번호를 이후 저장 정보에도 같이 보내줘야 저장될 수 있음
```python
def comments_create(request,pk):
    article = Article.object.get(pk=pk)
    comment_form = CommentFrom(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit = False)
        comment.article = article
        comment.save()
    return redirect(~~)
```
- 위의 방식으로 commit  이전의 객체에다가 article을 추가함으로써 저장 폼을 만족시킬 수 있다
- comment 삭제, 수정 관련 언급 존재
- 추가
  - 댓글 갯수 출력
    - length 사용
    - count() 사용
  - Default 값 부여
    - for - empty - endfor
    - 를 활용해서 없는 경우 부여 가능
### User - Article relationshiop
- setting.AUTH_USER_MODEL
  - settings에 있는 usermodel 정의
  - models.py 에서 user모델을 참조할때 활용
  - 문자열을 반환
- get_user_model()
  - 활성화된 user모델을 반환(custom 이면 custom을)
  - 객체를 반환
  - model을 제외한 나머지 곳에서 user모델을 참조할때 활용
- 이 외에는 대부분의 방법이 동일하다
- 삭제 경우에는, reqest.user == article.user의 조건을 추가
### Comment - User relationship
- user-comment 와 거의 거의 동일
- comment 에 user foreign key로 추가
- migrate (null값에 기본값 추가)
- modelform 에 exclude 추가
- view 에서 comment 에다가 user 추가 하는 과정 추가

### 마무리
- relationship (N:1)
- Foreign Key
- Django Relationship fields
- Related manager (특수 명령어)