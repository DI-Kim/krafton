year = int(input())

# 윤년 판단 함수
def isLeapYear(year):
    if year % 4 == 0:
        if year % 400 == 0:
            print(1)
            return
        elif year % 100 == 0:
            print(0)
            return
        print(1)
        
    else:
        print(0)
        
isLeapYear(year)