def welcome(u):
    print('ようこそ{}さん'.format(u['name']))
    u['age'] += 1
    print('あなたは来年{}際だから大吉です！'.format(u['age']))

username = input('名前を入力してください >>')
userage = int(input('年齢を入力してください >>'))
user = {'name': username, 'age': userage}
# user2 = {'name': user['name'], 'age': user['age']}
# user_message = user.copy()
# user_message = dict()
# for k, v in user.items():
#     user_message[k] = v
user_message = dict()
for k in user:
    user_message[k] = user[k]
welcome(user)
print('{}歳の{}さん、またプレイしてくださいね'.format(user_message['age'], user_message['name']))