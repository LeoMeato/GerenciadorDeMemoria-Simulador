from utilidades import decimal_binario
import os

def traduz(path):
    arq = open(path, "r")
    texto = arq.readlines()
    arq.close()
    texto_sub = []
    for i in range(len(texto)):
        parcial = []
        temp = texto[i].split()
        parcial.append(temp[0])
        parcial.append(temp[1])
        if len(temp) == 4:
            parcial.append(decimal_binario(temp[2]))
        texto_sub.append(parcial)

    arq = open("bin.txt", "w")
    
    for i in range(len(texto_sub)):
        arq.write(texto_sub[i][0] +" "+ texto_sub[i][1] + " " + str(texto_sub[i][2]+"\n"))

    arq.close()