from re import X


# def test_args(num1, *args, **kwargs):
#     print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
#     print(f'num1: {num1}')
#     print(f'args: {args}')
#     print(f'kwargs: {kwargs}')
# fruit_list = ['apple','banana','grape']
# test_args(123, 'hello', 'have', 'a', 'nice', 'day', fruit_list)
# test_args('hello', 'have', 'a', 'nice', 'day')
# test_args(fruit_list)
# test_args(*fruit_list)


# def test_kwargs(**kwargs):
#     print('===========================')
#     print(f'kwargs: {kwargs}')
# info = {"age":"90", "name":"옆집할머니", "car":"아이오닉", "num":"010-1234-5678", "address":"경기도"}
# test_kwargs(age='90', name='옆집할머니')
# test_kwargs(**info)
# test_kwargs(user=info)
# # test_kwargs(info) #> info 자체가 dict라서 args로 인식


def test(age, *args, **kwargs):
    if 'address' in kwargs:        
        arg_list = []
        
        for arg in args:
            arg_list.append(arg)
        print(arg_list)
        print(f'age: {age} // args: {args} // kwargs: {kwargs}')
    
test(90, "옆집할머니", "건치", "아이오닉", 성별="여성", num="010-1234-5678", address="경기도" )


# mutable : list
x = [1,2]
y = x
z = x[:]
y.append(3)
print(f'{x} : {id(x)}') # [1, 2, 3] 4315180032
print(f'{y} : {id(y)}') # [1, 2, 3] 4315180032
print(f'{z} : {id(z)}') # [1, 2] 4316070784