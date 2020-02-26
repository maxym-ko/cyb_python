# 21_1
def write_list(filename, lst):
    try:
        with open(filename, 'w') as f:
            for el in lst:
                f.write(str(el))
                f.write('\n')
    except OSError as e:
        return e.errno
    return 0


write_list('test.txt', [i for i in range(10)])


# 21_2
def read_to_list(filename):
    lst = []
    with open(filename) as f:
        for s in f:
            lst.append(int(s))
    return lst


print(read_to_list("test.txt"))
