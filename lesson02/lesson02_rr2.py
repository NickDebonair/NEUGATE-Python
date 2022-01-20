# ２．(オプション問題)　以下の二つのコレクションを用いてじゃんけんゲームプログラムを作成してください。
# コレクションをうまく使うと、簡潔なコードで完成できます。
# 「'あいこ', 'PC の勝ち', 'あなたの勝ち' 」
# 「 'ぐー', 'ちょき', 'ぱー' 」
#
# 実行例
#
# じゃんけんゲーム始めるよー
# PC と勝負です！
# あなたの手を数字で選んでください
# 0:ぐー 1:ちょき 2:ぱー
# >>0
# あなたの手は「ぐー」、PC の手は「ちょき」。
# あなたの勝ちです。
import random
hand_dic = {0: 'グー', 1: 'ちょき', 2: 'ぱー'}
hand = int(input('じゃんけんゲーム始めるよー'
                 '\nPC と勝負です！'
                 '\nあなたの手を数字で選んでください'
                 '\n0:ぐー 1:ちょき 2:ぱー'
                 '\n>>'))
hand_pc = random.randint(0, 2)
if hand == 0 and hand_pc == 1:
    print('あなたの手は「' + hand_dic[hand] + '」、PC の手は「' + hand_dic[hand_pc] + '」。')
    print('あなたの勝ちです')
elif hand == 1 and hand_pc == 2:
    print('あなたの手は「' + hand_dic[hand] + '」、PC の手は「' + hand_dic[hand_pc] + '」。')
    print('あなたの勝ちです')
elif hand == 2 and hand_pc == 0:
    print('あなたの手は「' + hand_dic[hand] + '」、PC の手は「' + hand_dic[hand_pc] + '」。')
    print('あなたの勝ちです')
elif hand == 0 and hand_pc == 2:
    print('あなたの手は「' + hand_dic[hand] + '」、PC の手は「' + hand_dic[hand_pc] + '」。')
    print('PCの勝ちです')
elif hand == 1 and hand_pc == 0:
    print('あなたの手は「' + hand_dic[hand] + '」、PC の手は「' + hand_dic[hand_pc] + '」。')
    print('PCの勝ちです')
elif hand == 2 and hand_pc == 1:
    print('あなたの手は「' + hand_dic[hand] + '」、PC の手は「' + hand_dic[hand_pc] + '」。')
    print('PCの勝ちです')
elif hand == 0 and hand_pc == 0:
    print('あなたの手は「' + hand_dic[hand] + '」、PC の手は「' + hand_dic[hand_pc] + '」。')
    print('あいこ')
elif hand == 1 and hand_pc == 1:
    print('あなたの手は「' + hand_dic[hand] + '」、PC の手は「' + hand_dic[hand_pc] + '」。')
    print('あいこ')
elif hand == 2 and hand_pc == 2:
    print('あなたの手は「' + hand_dic[hand] + '」、PC の手は「' + hand_dic[hand_pc] + '」。')
    print('あいこ')
result = hand - hand_pc
result_dic = {-1: 'あなたの勝ちです', 2: 'あなたの勝ちです', 1: 'PCの勝ちです', -2: 'PCの勝ちです', 0: 'おあいこ'}
print('あなたの手は「' + hand_dic[hand] + '」、PC の手は「' + hand_dic[hand_pc] + '」。')
print(result_dic[result])

'''
-1 % 3 は　2になるそうです。 -2 % 3 は　1になるそうです。
print()でやってみてください。
なので、
result_dicの'あなたは勝ちです'のキー-1,2は　% 3するとどちらも 2, 
result_dicの'PCの勝ちです'のキー-2,1は % 3するとどちらも 1
であることが分かります。
なので、タプルで、['おあいこ', 'PCの勝ちです', 'あなたの勝ちです']
としておいて、result % 3 をして、リストの順番を指定すれば、勝ち負けを指定できます。
'''
result_list = ['おあいこ', 'PCの勝ちです', 'あなたの勝ちです']


print('あなたの手は「' + hand_dic[hand] + '」、PC の手は「' + hand_dic[hand_pc] + '」。')
print(result_list[result % 3])

# print(hand)
# print(hand_dic[hand])
# print(hand_pc)
# print(hand_dic[hand_pc])
# 引き算した結果が0であれば、先頭の要素の先頭を出す。
