import re


def check(str):
    return [
        m.group(1)

        for m in re.finditer(
            r".*/\*(.+)\*/.*",
            str
        )
    ]


print(check("/*Mateus Moreira de Sousa*/"))
