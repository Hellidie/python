from Crypto.Util.number import *    # pip install pycryptodome

p = getPrime(64)                    # getPrime(N) генерирует случайное простое число длиной N бит
q = getPrime(64)
e = 65537

n = p * q
f = (p - 1) * (q - 1)
d = inverse(e, f)

dict_open = {                       # открытый ключ
    "e": e,
    "n": n
}

dict_closed = {                     # закрытый ключ
    "d": d,
    "n": n
}

print(dict_open, dict_closed)

flag = bytes("flag", encoding='utf-8')
message = bytes_to_long(flag)
c = (message ** e) % n              # шифруем сообщение
print(c)


