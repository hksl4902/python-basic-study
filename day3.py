#3일차 02-5(딕셔너리 자료형) 02-6(집합 자료형)

#딕셔너리 자료형 기본 모습({key1: Vaule1})

a={1: 'a'}
a[2]='b'
print(a)
a['name']='pey'
print(a)
a[3]=[1,2,3]
print(a)
del a[1]
print(a)
grade={'pey':10,'julliet':99}
print(grade['pey'])
print(grade['julliet'])
a={1:'a',2:'b'}
print(a[1])
print(a[2])
a={'a':1,'b':2}
print(a['a'])
print(a['b'])
#중복된 key값으로 설정하면 하나를 제외하고 나머지 것들은 다 무시됨
#key
a={'name':'pey','phone':'010-0000-1234','brith':'1118'}
print(a.keys())
#vaule
print(a.values())
#key,vaule 한번에 item
print(a.items())
#clear
a.clear()
print(a)
#get
a={'name':'pey','phone':'010-0000-1234','brith':'1118'}
print(a.get('name'))
print(a.get('phone'))
#in
print('name' in a)
print('email' in a)


#02-6 집합 자료형
s1=set([1,2,3])
print(s1)
s2=set("hello")
print(s2) #중복 허용 x 순서 x
l1=list(s1)
print(l1)
print(l1[0])
t1=tuple(s1)
print(t1)
s1=set([1,2,3,4,5,6,])
s2=set([4,5,6,7,8,9])
print(s1&s2)
print(s1.intersection(s2))
print(s1|s2)
print(s1.union(s2))
print(s1-s2) #difference 함수 사용해도 동일
print(s2-s1)
#add
s1=set([1,2,3])
s1.add(4)
print(s1)
#update
s1=set([1,2,3])
s1.update([4,5,6])
print(s1)
#remove
s1=set([1,2,3])
s1.remove(2)
print(s1)