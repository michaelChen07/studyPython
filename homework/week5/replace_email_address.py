#conding=utf-8

import re

def passwords_strength():
    passwords = raw_input("please input password:")
    if len(passwords) >= 8:
        print len(passwords)
        if re.search(r"^\d+&",passwords) or re.search(r"^[A-Za-z]+$",passwords):
            return "low"
        elif re.search(r"^\d+[A-Za-z]+$",passwords) or re.search(r"^[A-Za-z]+\d+$",passwords):
            return "middle"
        else:
            return "high"
    else:
        return "low"

print passwords_strength()