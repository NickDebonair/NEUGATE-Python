qq = []
# qq_list = list()
for i in range(1, 10):
    # qq_list.append(i)
    # qq.append(qq_list)
    qq_list = list()

    for j in range(1, 10):
        qq_list.append(i * j)
    qq.append(qq_list)
# for j in range(1, 10):
    # qq_list * j
    # qq_list2.append(j)
    # qq.append(qq_list)

print(qq)
print(qq_list)
for q in qq:
    print(q)
