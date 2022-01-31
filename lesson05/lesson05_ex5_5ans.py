def int_input(msg):
    num = int(input('{}を入力してください >>'.format(msg)))
    return num

def calc_payment(amount, people=2):
    dnum = amount / people
    pay = dnum // 100 * 100
    if dnum > pay:
        pay = int(pay + 100)
    payorg = amount - pay * (people - 1)
    return pay, payorg

def show_payment(pay, payorg, people=2):
    print('1人あたり{}円({}人)、幹事は{}円です。'.format(pay, people-1, payorg))

amount = int_input('支払総額')
people = int_input('参加人数')

pay, payorg = calc_payment(amount, people)

show_payment(pay, payorg, people)