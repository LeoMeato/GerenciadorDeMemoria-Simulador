# Binario pra Decimal
def binario_decimal(binario):
    binario[::-1]
    decimal = 0
    for i in range(len(binario)):
        decimal += (int(binario[i])) * (2**i)
    return decimal
