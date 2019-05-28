# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-05-28 17:24

import string

# result = string.ascii_letters
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# result = string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'

# result = string.ascii_uppercase
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# result = string.digits
# '0123456789'

result = string.hexdigits
# '0123456789abcdefABCDEF'

# result = string.letters
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# result = string.lowercase
# 'abcdefghijklmnopqrstuvwxyz'

# result = string.uppercase
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# result = string.octdigits
# '01234567'

# result = string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# result = string.printable
# '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

# result = string.whitespace
# '\t\n\x0b\x0c\r

#  生成随机数
import random,string
def genRandomString(slen=10):
    return ''.join(random.sample(string.punctuation + string.ascii_letters + string.digits, slen))

res = genRandomString()
print(res)
print(''.join(random.sample(string.printable,10)))