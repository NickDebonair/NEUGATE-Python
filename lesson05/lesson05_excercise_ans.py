def get_japanese_season(month):
    season = ''
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
