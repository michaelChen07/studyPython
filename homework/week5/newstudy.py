#encoding=utf-8
import re

str2int = lambda s: int(s + '1' * (not s[-1:].isdigit()))


def monomial(args):
    ('-5', '4')
    c, p = map(str2int, args)
    return '%+d' % (c * p) + 'x' * (p > 1) + '^%d' % (p - 1) * (p > 2)


def derivative(eq):
    [('-5', '4'), ('4', '2'), ('-', '')]
    return ''.join(map(monomial, re.findall("(-?\d*)x\^?(\d*)", eq))).lstrip('+') or '0'


if __name__ == "__main__":
    t = '-5x^4+4x^2-x+11'
    print derivative(t)








