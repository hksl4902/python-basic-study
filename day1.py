#1일차 점프 투 파이썬 참고 02-1(숫자형) 02-2(문자열 자료형)


#숫자형

#8진수
a=0o177
print(a)

#16진수
a=0x8ff
b=0xABC
print(b)
print(a)

#연산자
a=3
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(7%3)
print(3%7)

#문자열 자료형

#따옴표
food="python\'s favorite food is perl"
print(food)
say="\"pyton is very easy.\"he says."
print(say)
multiline="life is too short\nyou need python"
print(multiline)
m='''
life
short
'''
print(m)

#문자열 연산
head="python"
tail=" is fun!"
print(head+tail)

a="python"
print(a*2)

a="life is too short"
print(len(a))

b="you need python"
print(len(b))

#문자열 인덱싱
a="life is too short, you need python"
print(a[3])
print(a[0])
print(a[-1])
print(a[-0])
a="life is too short, you need python"
b=a[0]+a[1]+a[2]+a[3]
print(b)
print(a[0:4])
a="life is too short, you need python"
print(a[:2])
print(a[:])
a="20260122Sunny"
year=a[:4]
day=a[4:8]
weather=a[8:]
print(year,day,weather)

#문자열 포매팅
print("I eat %d apples." %3) #숫자열 삽입은 %d-정수
print("I eat %s apples." %"five") #문자열 삽입은 %s
number=3
print("I eat %d apples." %number)
number=10
day="three"
print("I ate %d apples. so I was sick for %s days." %(number,day))

#포맷 코드
#정렬
print("%10s" % "hi") #오른쪽 정렬
print("%-10sjane."% 'hi') #왼쪽 정렬
#소수점
print("%0.4f" % 3.42134234) #소수점 네번째 자리
print("%10.4f" % 3.42134234) #공백 4개 소수점 네번째 자리

#format 함수
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
number=10
day="three"
print("I eat {0} apples. so I was sick for {1} days.".format(number,day))
print("I eat {number} apples. so I was sick for {day} days.".format(number=2,day=6))
print("{0:<10}".format("hi"))#왼쪽
print("{0:>10}".format("hi"))#오른쪽
print("{0:^10}".format("hi"))#중간
print("{0:=^10}".format("hi"))
name='lsy'
age=20
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')#f문자열 포매팅
print(f'{"python":!^12}')
#문자열 관련 함수
a="hobby"
print(a.count('b'))#count 함수 문자개수

a="Python is the best choice"
print(a.find('b')) #find함수 위차함수

a="life is too short"
print(a.index('t'))#index함수 위치함수

print(",".join('abcd'))#join함수 문자삽입

a="hi"
print(a.upper())#upper 함수 대문자로

a="HI"
print(a.lower())#lower함수 소문자로

a="  hi  "
print(a.lstrip())#공백관련함수 lstrip은 왼쪽 공백 지움 rstrip은 오른쪽 공백 지움 strip은 양쪽 공백 지움
print(a.rstrip())
print(a.strip())

a="life is too short"
print(a.replace("life","your leg"))#replace함수 대체함수

a="life is too short"
print(a.split()) #split함수 문자열 나누기