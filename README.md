# djangsamo
<hr />

## 과제(6/21)
<details>
<div markdown="1">
</br>
1. product라는 앱을 새로 생성해주세요</br>
2. product 앱에서 <작성자, 제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일>가 포함된 product 테이블을 생성해주세요</br>

3. django serializer에서 기본적으로 제공하는 validate / create / update 기능을 사용해 event 테이블의 생성/수정 기능을 구현해주세요</br>
   * postman으로 파일을 업로드 할 때는 raw 대신 form-data를 사용하고, Key type을 File로 설정해주세요</br>

4. 등록된 이벤트 중 현재 시간이 노출 시작 일과 노출 종료 일의 사이에 있거나, 로그인 한 사용자가 작성한 product 쿼리셋을 직렬화 해서 리턴해주는 serializer를 만들어주세요</br>

5. product field를 admin에서 관리할 수 있도록 등록해주세요</br>
</div>
</details>

## 과제(6/20)
<details>
<div markdown="1">
</br>
1. admin 페이지에 user admin을 등록하고, userprofile 테이블을 user admin 페이지에서 같이 보고 설정 할 수 있도록 해주세요</br>
2. article 테이블에 <노출 시작 일자, 노출 종료 일자>를 추가해주세요</br>
3. article view에 게시글 조회 기능을 만들되, 현재 일자를 기준으로 노출 시작 일자와 노출 종료 일자 사이에 있는 항목들만 리턴해주도록 필터를 설정해주세요</br>
 - 리턴 데이터는 게시글 작성일 기준으로 정렬하여 최근 쓴 글이 가장 먼저 올라오도록 해주세요</br>
4. 기존 article 생성 기능을 유지하되, article은 admin user 혹은 가입 후 7일이 지난 사용자만 생성 가능하도록 해주세요</br>
 - 조회는 로그인 한 사용자에 대해서만 가능하도록 설정해주세요</br>
</div>
</details>

## 과제(6/17-19)
<details>
<div markdown="1">
</br>
1. blog 앱에 <게시글, 사용자, 내용>이 포함된 comment 테이블을 작성해주세요</br>
2. 외래 키를 사용해서 Article, User 테이블과 관계를 맺어주세요</br>
3. admin.py에 comment를 추가해 자유롭게 생성, 수정 할 수 있도록 해주세요</br>
4. serializer를 활용해 로그인 한 사용자의 기본 정보와 상세 정보를 리턴해 주는 기능을 만들어주세요</br>
5. 4번의 serializer에 추가로   로그인 한 사용자의 게시글, 댓글을 리턴해주는 기능을 구현해주세요</br>
5. blog 앱에 title / category / contents를 입력받아서 게시글을 작성하는 기능을 구현해주세요</br>
 - 만약 title이 5자 이하라면 게시글을 작성할 수 없다고 리턴해주세요</br>
 - 만약 contents가 20자 이하라면 게시글을 작성할 수 없다고 리턴해주세요</br>
 - 만약 카테고리가 지정되지 않았다면 카테고리를 지정해야 한다고 리턴해주세요</br>
6. custom permission class를 활용해 가입 후 3일 이상 지난 사용자만 게시글을 쓸 수 있도록 해주세요</br>
 - 테스트 할 때에는 가입 후 3분 이상 지난 사용자가 게시글을 쓸 수 있게 해주세요</br>
 - join_date는 datetime field로 만들어주세요</br>
</div>
</details>

## 과제(6/16)
<details>
<div markdown="1">
</br>
1. Django 프로젝트를 생성하고, user 라는 앱을 만들어서 settings.py 에 등록해보세요.</br>
2. user/models.py에 `Custom user model`을 생성한 후 django에서 user table을 생성 한 모델로 사용할 수 있도록 설정해주세요</br>
3. user/models.py에 사용자의 상세 정보를 저장할 수 있는 `UserProfile` 이라는 모델을 생성해주세요</br>
4. blog라는 앱을 만든 후 settings.py에 등록해주세요</br>
5. blog/models.py에 <카테고리 이름, 설명>이 들어갈 수 있는 `Category`라는 모델을 만들어보세요.</br>
6. blog/models.py에 <글 작성자, 글 제목, 카테고리, 글 내용>이 들어갈 수 있는 `Article` 이라는 모델을 만들어보세요.</br>(카테고리는 2개 이상 선택할 수 있어야 해요)</br>
7. Article 모델에서 외래 키를 활용해서 작성자와 카테고리의 관계를 맺어주세요</br>
8. admin.py에 만들었던 모델들을 추가해 사용자와 게시글을 자유롭게 생성, 수정 할 수 있도록 설정해주세요</br>
9. CBV 기반으로 로그인 / 로구아웃 기능을 구현해주세요</br>
10. CBV 기반으로 로그인 한 사용자의 게시글의 제목을 리턴해주는 기능을 구현해주세요</br>
</div>
</details>

## 과제(6/15)
<details>
<summary> 1. args, kwargs를 사용하는 예제 코드 짜보기 > args를 리스트화하기</summary>
<div markdown="1">
 </br>
 
```python
def test(age, *args, **kwargs):
    if 'address' in kwargs:        
        arg_list = []
        for arg in args:
            arg_list.append(arg)
        print(arg_list)
        print(f'age: {age} // args: {args} // kwargs: {kwargs}')
    
test(90, "옆집할머니", "건치", "아이오닉", 성별="여성", num="010-1234-5678", address="경기도" )
```
 
</div>
</details>
<details>
<summary>2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기</summary>
<div markdown="1">
</br>
수정이 가능한 객체를 'mutable' 부름 > list, dict, Set</br>
수정이 불가능한 객체를 'immutable' 부름 > int, float, bool, str, tuple</br>
y = x , z = x 부분에서 같은 주소를 가리키게 되어 둘의 값은 동일해진다. </br>
`[:]나 deepcopy` 를 사용하면 같은 객체를 공유하지 않는 것이 가능하다.</br>

```python
# mutable : list
x = [1,2]
y = x
z = x[:]
y.append(3)
print(f'{x} : {id(x)}')     # [1, 2, 3] 4315180032
print(f'{y} : {id(y)}')     # [1, 2, 3] 4315180032
print(f'{z} : {id(z)}')     # [1, 2] 4316070784
```

</div>
</details>
<details>
<summary>3. DB Field에서 사용되는 Key 종류와 특징 서술하기</summary>
<div markdown="1">
 </br>
 
* Primary Key 기본키 : null 값을 가질 수 없으며 동일한 값이 중복될 수 없다.</br>
*  Alternate Key 대체키 : 후보키가 둘 이상일 경우, 기본키를 제외한 키</br>
* Candidate Key 후보키 : 유일성과 최소성을 만족하는 속성 또는 속성들의 집합으로 기본키가 될 수 있는 조건을 가진 키</br>
* Super Key 수퍼키 : 유일성의 특성을 만족하는 속성 또는 속성들의 집합</br>
* Foreign Key 외래키 : 두 테이블을 함께 쓸 때 연결하는 키</br>

</div>
</details>
<details>
<summary> 4. django에서 queryset과 object는 어떻게 다른지 서술하기</summary>
<div markdown="1">
 </br>
 DB에는 스키마도 있고, row와 column로 이루어져있다.</br>
각 object들은 DB에서 하나의 record(row)에 해당한다.</br>
딕셔너리 형태로 이루어져 key와 value 값이 있다.</br>
아래의 코드로 key와 value값에 접근이 가능하다.</br>

```python
 <variable name>[index]['key']
 .values()
 ```
 
 queryset은 리스트형식으로 all()을 사용해 모든 objects에 접근한다.</br>
filter(), all()은 list로 반환하기때문에 index로 접근할 수 있다.</br>

</div>
</details>

 
 


 




