#4일차 02-7(불 자료형), 02-8(변수)

#02-7 불 자료형-참과 거짓을 나타내는 자료형

a=True
b=False

print(type(a))
print(type(b))
print(1==1)
print(2>1)
print(2==1)
#문자열,리스트,튜플,딕셔너리 값이 비어 있으면 거짓, 숫자는 0일때 거짓
a=[1,2,3,4]
while a:
    print(a.pop())

if [1,2]:
    print("참")
else:
    print("거짓")
print(bool("py"))
print(bool(''))


#02-8 변수
c=[1,2,3]
print(id(c))

a=[3,5,5]
a=b
print(id(a))
print(id(b))
print(a is b)   
#서로 다른 값을 주게 하기
a=[1,2,3]
b=a[:]
a[1]=4
print(a)
print(b)

#copy모듈 활용
from copy import copy
a=[1,2,3]
b=copy(a)
print(b is a)