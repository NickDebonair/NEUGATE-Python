def is_leapyear(num):
    leapyear = False
    if num % 400 == 0:
        leapyear = True
    elif num % 4 == 0:
        if num % 100 == 0:
            leapyear = False
        else:
            leapyear = True
    return leapyear

msg = ''
# while True:
#     year = int( input('何年を調べますか？'))
#     if is_leapyear(year):
#         msg = 'うるう年です'
#     else:
#         msg = 'うるう年ではありません'
#
#     print('西暦{}年は、'.format(year) + msg)

year_list = [int(x) for x in input().split()]
print(year_list)
year_msg = []
year_elem = ''
year_dict = {}
for i in year_list:
    if is_leapyear(i):
        year_elem = 'うるう年です'
    else:
        year_elem = 'うるう年ではありません'
    year_msg.append(year_elem)
print(year_msg)

for j in range(len(year_list)): #リストの要素の数でfor文で回す
    print('西暦{}年は、'.format(year_list[j]) + year_msg[j])

year_dict = dict(zip(year_list, year_msg)) #2つのリストをディクショナリに融合させる方法
for k, v in year_dict.items(): # ディクショナリのキーとバリューの要素でfor文ループｊ
    print('西暦{}年は、{}'.format(k, v))