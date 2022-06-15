# djangsamo
과제(6/15)
<details>
<summary> 1. args, kwargs를 사용하는 예제 코드 짜보기 > args를 리스트화하기</summary>
<div markdown="1">
 </br>
 
```
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
[:]나 deepcopy를 사용하면 같은 객체를 공유하지 않는 것이 가능하다.</br>

```
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

```
 <variable name>[index]['key']
 .values()
 ```
 
 queryset은 리스트형식으로 all()을 사용해 모든 objects에 접근한다.</br>
filter(), all()은 list로 반환하기때문에 index로 접근할 수 있다.</br>

</div>
</details>

 
 


 




