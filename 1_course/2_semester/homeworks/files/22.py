# 22_3 (22_2_b)
import sys


def read_to_list(filename):
    lst = []
    err_n = 0
    with open(filename) as f:
        for s in f:
            try:
                s = s.strip()  # additional (to complete 22_3)
                if s != '':  # additional (to complete 22_3)
                    lst.append(int(s))
            except ValueError as e:
                err_n += 1
                sys.stderr.write(repr(e) + '\n')
    return lst, err_n


print(read_to_list("files/test.txt"))


# 22_6
def write_lst(filename):
    lst = []
    with open(filename) as f:
        for s in f:
            if s.strip() != '':
                try:
                    lst.append(int(s))
                except ValueError:
                    lst.append(float(s))
    return lst


print(write_lst("files/test.txt"))


# 22_7
def analyze(filename):
    res = [0, 0, 0, 0]
    with open(filename) as f:
        for s in f:
            res[get_kind(s)] += 1
    return {'int_count': res[0], 'float_count': res[1], 'blank_count': res[2], 'err_count': res[3]}


def get_kind(s):
    if s.isspace():
        return 2
    try:
        int(s)
        return 0
    except ValueError:
        try:
            float(s)
            return 1
        except ValueError:
            return 3


print(analyze("files/test.txt"))


# 22_8
def write_pairs_to_lst(filename):
    lst = []
    with open(filename) as f:
        for s in f:
            lst.append((float(s.split()[0]), float(s.split()[1])))
    return lst


print(write_pairs_to_lst("files/test.txt"))
