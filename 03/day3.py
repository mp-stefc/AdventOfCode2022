

def split_half(line):
    middle = int(len(line)/2)
    a, b = line[:middle], line[middle:]
    assert len(a) == len(b)
    return a,b

def find_dup(l1, l2):
    return (set(l1) & set(l2)).pop()

def prio(char):
    # 'A' has ascii 65, mapping to 27
    mapping_shift = 38 if char.isupper() else 96
    return ord(char) - mapping_shift

with open("input", "r") as f:
    lines = f.readlines()
    sum_prios=0
    for line in lines:
        l1, l2 = split_half(line.strip())
        dup = find_dup(l1,l2)
        sum_prios = sum_prios + prio(dup)

    print(sum_prios)



