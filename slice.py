# -*- coding: utf-8 -*-
def trim(s):
    if len(s) == 0 or (s[-1] != ' ') and (s[0] != ' '):
        return s
    elif s[-1] == ' ':
        return trim(s[:-1])
    elif s[0] == ' ':
        return trim(s[1:])

# 测试
if trim('hello  ') != 'hello':
    print('failed!')
elif trim('  hello') != 'hello':
    print('failed!')
elif trim('  hello  ') != 'hello':
    print('failed!')
elif trim('') != '':
    print('failed!')
elif trim('    ') != '':
    print('failed!')
else:
    print('成功')


# s='ABCDEFG'
# print(s[1:])  #BCDEFG
# print(s[:-1]) # ABCDEF


