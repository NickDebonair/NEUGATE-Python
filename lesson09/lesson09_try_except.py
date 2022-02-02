while True:
    try:
        price = int(input('料金を入力 >>'))
        number = int(input('人数を入力 >>'))
        print('1人あたり{}円です'.format(price / number))
        break
    except ValueError:
        print('料金または人数に整数を入力してください')
    except ZeroDivisionError:
        print('人数に0を入力しないでください')

print('プログラムを終了します')
