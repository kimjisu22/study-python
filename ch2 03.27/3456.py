# num = int(input('숫자를 입력하세요.'))

# if num > 10:
#     print('num은 10보다 크다')
#     print('num: ', num)

# number = 0
# if number > 0:
#     print('양수')

# if number > 0: print('양수')

# score = int(input('점수를 입력하세요'))

# if score >= 80:
#     print('합격입니다')

# else:
#     print('아쉽')

# score = int(input('점수를 입력하세요'))

# if score >= 80:
#     pass
# else:
#     pass

# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket:
#     print('택시를 타고 가라')

# else:
#     print("걸어가")

# x in s, x not in s
# print(1 in [1,2,3])
# print(1 not in [1,2,3])

# print('a' in('a','b','c'))
# print('j' not in 'python')

# temp = int(input('기계 온도를 입력하세요'))

# if temp >= 40:
#     print('팬가동')
# else:
#     print('팬중지')

# score = int(input('점수를 입력하세요'))

# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')

# num = int(input('양의 정수를 구하시오'))

# if num > 0:
#     print('num: ',num)

#     if num % 2 == 0:
#         print("양의 정수입니다")
#     else:
#         print('홀수입니다')
# else:
#     print("num은 야의 정수가 아니다")

# 버스전용차로에 버스가 아닌 승용차가 주행할 경우 단속 토요일 공휴일은 단속을 하지 않음
# print("1.월~금, 2.토요일, 3.공휴일")
# week = int(input("요일을 선택하세요"))

# if week == 1:
#     print("단속")
#     print("1.버스 2. 승용차")
#     car = int(input("차종을 선택"))

#     if car == 1:
#         print("버스")
#     else:
#         print("위반")

# else:
#     print("단속안함")

# 출생연도 끝자리와 나이를 입력하면 다음 요구사항에 맞춰 마스크 구매 가능한 요일을 출력
# 만 65세 노인은 언제든지 구매 가능

# year = int(input("출생연도 끝자리를 입력하세요: "))
# age = int(input("만 나이 입력: "))
# if age <= 65:
#     if year == 1 or year == 6:
#         print("월요일에 구매 가능")
#     elif year == 2 or year == 7:
#         print("화요일에 구매 가능")
#     elif year == 3 or year == 8:
#         print("수")
#     elif year == 4 or year == 9:
#         print("목")
#     elif year == 5 or year == 0:
#         print("금")
#     else:
#         print("언제든지 가능")

# 조건문 실전예제1
today = int(input("오늘 날짜를 입력하세요: "))

num = int(input("차량번호 4자리를 입력하세요: "))
