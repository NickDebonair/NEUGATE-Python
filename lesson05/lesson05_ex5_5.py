def int_input():
    amount = int(input('支払総額を入力してください >>'))
    people = int(input('参加人数を入力してください >>'))
    return amount, people

def calc_payment(amount, people):
    dnum = amount / people
    pay = dnum // 100 * 100
    if dnum > pay:
        pay = int(pay + 100)
    payorg = amount - pay*(people - 1)
    return dnum, pay, payorg

def show_payment(pay, people, payorg):
    print('*** 支払額 ***')
    print('1人あたり{}円({}人)、幹事は{}円です。'.format(pay, people-1, payorg))


amount, people = int_input()
dnum, pay, payorg = calc_payment(amount, people)
show_payment(pay, people, payorg)
