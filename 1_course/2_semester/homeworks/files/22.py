# 22_3 (22_2_b)
import sys


def read_to_list(filename):
    lst = []
    err_n = 0
    with open(filename) as f:
        for s in f:
            try:
                s = s.strip()  # additional (to complete 22_3)
                if s != '':    # additional (to complete 22_3)
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
    res = {'int_count': 0, 'float_count': 0, 'blank_count': 0, 'err_count': 0}
    with open(filename) as f:
        for s in f:
            try:
                int(s)
                res['int_count'] += 1
            except ValueError:
                try:
                    float(s)
                    res['float_count'] += 1
                except ValueError:
                    if s.strip() != '':
                        res['err_count'] += 1
                    else:
                        res['blank_count'] += 1
    return res


print(analyze("files/test.txt"))


# 22_8
def write_pairs_to_lst(filename):
    lst = []
    with open(filename) as f:
        for s in f:
            a = ''
            b = ''
            for i in range(len(s)):
                if '0' < s[i] < '9':
                    a += s[i]
                else:
                    b += s[i:].strip()
                    break
            lst.append((a, b))
    return lst


print(write_pairs_to_lst("files/test.txt"))
