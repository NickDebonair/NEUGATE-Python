def split_bill():
    try:
        price = int(input('料金を入力 >>'))
        number = int(input('人数を入力 >>'))
        print('1人あたり{}円です'.format(price / number))
    except ValueError:
        print('料金または人数に整数を入力してください')
        split_bill() # 再帰 オーバーフローになる前にPythonが止めてくれる　デフォルトで1000回、設定で2000回まで再帰できる。
    except ZeroDivisionError:
        print('人数に0を入力しないでください')
        split_bill() # 再帰 オーバーフローになる前にPythonが止めてくれる　デフォルトで1000回、設定で2000回まで再帰できる。

split_bill()
print('プログラムを終了します')
