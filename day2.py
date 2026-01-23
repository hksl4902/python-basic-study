#2일차 점프 투 파이썬 참고 02-3(리스트 자료형), 02-4(튜플 자료형)

#리스트 자료형

#리스트명 = [요소1, 요소2, 요소3]

a=[1,2,3]
print(a)
print(a[0])
print(a[0]+a[2])
print(a[-1])

a=[1,2,3,['a','b','c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0]) #이러면 a가 나옴

a=[1,2,3,['a','b',['life','is']]]
print(a[-1][2][0])

#슬라이싱
a=[1,2,3,4,5]
print(a[0:2])
print(a[1:3])
#연산
a=[1,2,3]
b=[4,5,6]
print(a+b)
a=[1,2,3]
print(a*3)
print(len(a))
#수정
a=[1,2,3]
a[2]=4
print(a)
#삭제
a=[1,2,3]
del a[1]
print(a)
a=[1,2,3,4,5]
del a[:2]
print(a)
#관련함수
#append 추가함수
a=[1,2,3]
a.append(4)
print(a)
a.append([5,6])
print(a)
#sort함수 정렬함수
a=[1,4,3,2]
a.sort()
print(a)
a=['c','a','b']
a.sort()
print(a)
#reverse 뒤집기 함수
a=['a','b','c']
a.reverse()
print(a)
#index 위치값 반환
a=[1,2,3]
print(a.index(3))
print(a.index(1))
#insert 삽입
a=[1,2,3]
a.insert(0,4)
print(a)
a.insert(2,5)
print(a)
#remove 제거
a=[1,2,3,1,2,3]
a.remove(3)
print(a)
#pop 
a=[1,2,3]
a.pop()
print(a)
#count
a=[1,2,3,1]
print(a.count(1))
#extend 확장
a=[1,2,3]
a.extend([4,5])
print(a)

#튜플 자료형 
# #리스트는 [] 튜플은 () 또 튜플은 요솟값이 변하지 않음
t1=(1,2,'a','b')
print(t1[2])
print(t1[3])
print(t1[1:])
t2=(3,4)
t3=t1+t2
print(t3)
t3=t2*3
print(t3)
print(len(t1))