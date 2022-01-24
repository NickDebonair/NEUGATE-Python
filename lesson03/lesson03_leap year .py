# （1）西暦が4で割り切れる年をうるう年とする
# （2）西暦が100で割り切れて、400で割り切れない年は、平年とする

# year = int(input('西暦何年が知りたいですか？'))
#
# msg = ''
#
# if year % 4 == 0:
#     if year % 100 == 0 and year % 400 != 0:
#         msg = '平年です'
#     else:
#         msg = 'うるう年です'
# else:
#     msg = '平年です'
#
# print(msg)



# year_list = [int(x) for x in input().split()]
year_list = []
year_list_elem = input().split()
print(year_list_elem)
for x in year_list_elem:
    year_list.append(int(x))
print(year_list)
year_msg = []
year_dict = {}
year_elem = ''
for y in year_list:
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            year_elem = '平年です'
        else:
            year_elem = 'うるう年です'
    else:
        year_elem = '平年です'
    year_msg.append(year_elem)
print(year_list)
print(year_msg)
year_dict = dict(zip(year_list, year_msg))
print(year_dict)


# うるう年を表示する問題で、一年一年入力して表示するのではなく、例えば、「2022 2021 2020 1990」など複数年一度に入力して、結果を出せるプログラミングを書いてみました。
# 入力する際は、スペースで区切ります。何年分でも大丈夫です。