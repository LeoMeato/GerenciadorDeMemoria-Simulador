# Binario pra Decimal
def binario_decimal(str):
    
    n = 0

    i = 0
    for bit in reversed(str):

        if bit == "1":
            n += 2**i
        i += 1
    return n

dic = {

    "n": 1,
    "al": 52,
    "nya": 8653,
    "low": 64531
}

for i in dic.values():
    print(i)