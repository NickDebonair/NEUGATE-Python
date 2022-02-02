file = open('sample.txt', 'r')
file2 = open('sample_copy.txt', 'a')
for line in file:
    print(line, end='')
    # file2.write(line)
file.close()
file2.close()