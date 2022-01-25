import random

hands = ('ぐー', 'ちょき', 'ぱー')

user_hand = int(input('>>'))
pc_hand = random.randint(0, 2)
print('あなたの手は「' + hands[user_hand] + '」、')
print('PCの手は「' + hands[pc_hand] + '」。')

result_tpl = ("あいこ", "PCの勝ち", "あなたの勝ち")
result_num = (user_hand - pc_hand + 3) % 3
print(result_tpl[result_num])