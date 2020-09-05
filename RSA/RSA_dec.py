from Crypto.Util.number import *

n = 166468446875550415955058029183055341987
d = 47357030739090314701388881792350698273
c = 69192509360332715222955396479366350012

m = pow(c, d, n)
print(m)
m = long_to_bytes(m)
print(m)
b = bytes.decode(m, encoding='utf-8')
print(b)
