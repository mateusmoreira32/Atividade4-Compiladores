import re


def check(str):
    return re.sub(r'(\w+)\:\s(\w+)', r'\g<2>: \g<1>', str)


print(check("key1: 11224 \nkey2: 524 \nkey3: 5125 \nAbc: 51252"))
