text = input('何を記録しますか？ >>')
file = open('diary.txt', 'a')
file.write(text + '\n')
file.close() # ストリーム⇒開いたら必ず閉じておかないといけない