# 関数定義
# 処理はインデントでブロックとして記述
def hello(name): # nameを記述している部分を、仮引数といいます
    print('こんにちは、{}です。'.format(name))
    print('よろしく!')
# 関数呼び出し
hello('高橋') # '高橋'を記述している部分を実引数といいます
hello('鈴木')
hello('佐藤')
hello('田中')

def plus(x, y):
    answer = x + y
    return answer

answer = plus(100, 50)
print(answer)