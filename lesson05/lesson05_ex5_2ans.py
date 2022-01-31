def is_leapyear(year):
    # result = False

    # if year % 400 == 0:
    #     # result = True
    #     return True
    # if year % 100 == 0:
    #     # result = False
    #     return False
    # if year % 4 == 0:
    #     # result = True
    #     return True
    # else:
    #     # result = False
    #     return False
    # return result
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

year = int(input('西暦を入力>>'))
# result = is_leapyear(year)
if is_leapyear(year):
    print('うるう年')
else:
    print('平年')
