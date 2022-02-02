num=0
def test():
    global num
    num += 1
    print(num)
    test()

test()