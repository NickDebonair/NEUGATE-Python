year = int(input('西暦を入力>'))
result = '平年'

if year % 400 == 0:
    result = 'うるう年'
elif year % 100 == 0:
    result = '平年'
elif year % 4 == 0:
    result = 'うるう年'
else:
    result = '平年'

# if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#     result = 'うるう年'

print(result)