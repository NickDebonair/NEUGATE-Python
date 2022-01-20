# 2.　(オプション問題)　プログラミングでは「割り算の余り」を使う場面が多くあります。演算子「%」を使ってみましょう。
#  入力された整数を、漢数字まじりにして表示するプログラムを作成してください。
#  *入力数値によって不自然な出力になっても構いません。（0兆0億123万4567 など）
#
# 実行例_1
# 9999兆までの数値を整数で入力してください。>>123456789012345
# 123兆4567億8901万2345
#
# 実行例_2
# 9999兆までの数値を整数で入力してください。>>1234567
# 0兆0億123万4567
value = int(input("9999兆までの数値を整数で入力してください。>>"))
v1 = value // 1000000000000
v2 = value % 1000000000000 // 100000000
v3 = value % 1000000000000 % 100000000 // 10000
v4 = value % 10000
print( str(v1) + '兆' + str(v2) + '億' + str(v3) + '万' + str(v4))