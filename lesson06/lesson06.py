msg = 'HELLO world!'
msg2 = 'HELLO world!'
if msg == msg2:
    print('（文字列比較）同じ')
else:
    print('（文字列比較）違う')
if id(msg) == id(msg2):
    print('同じ')
else:
    print('違う')


print(msg.capitalize())
print(msg.lower())
print(msg.upper())
print(msg.title())
print(msg.strip())
print(msg.split(' '))
print(msg.replace('world', 'python'))
print(msg.upper().count('L'))

def add(x, y):
    return x + y

print(type(add))
newadd = add
print(newadd(4, 5))