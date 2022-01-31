# 問題1.
# if 文を用いた条件分岐
# 分岐の条件式を正しく書き、if文のバリエーション構文も使えるようになりましょう。
# 1～12 の範囲で月を入力すると、日本での季節を表示するプログラムを、「if~elif~」構文を用いて作成してください。
# （3,4,5 月は春、6,7,8 月は夏、9,10,11 月は秋、12,1,2 月は冬を表示）
#
# 実行例
#
# 1～12 の範囲で月を入力してください。>>3
# 日本の3 月は、春です。
def season_disc(month):
    global season
    if month < 3 or month == 12:
        season = '冬'
    elif month < 6:
        season = '春'
    elif month < 9:
        season = '夏'
    elif month < 12:
        season = '秋'
    return season

month = int(input('1～12 の範囲で月を入力してください。>>'))
season = season_disc(month)
print('日本の'+str(month)+'月は、'+ season+'です。')
