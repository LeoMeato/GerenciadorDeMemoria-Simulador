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
        parcial.append(str(temp[0]))
        parcial.append(str(temp[1]))
        if len(temp) == 4:
            parcial.append(str(decimal_binario(temp[2])))
        texto_sub.append(parcial)

    arq = open("bin.txt", "w")
    
    
    for i in range(len(texto_sub)):
        text = texto_sub[i][0] +" "+ texto_sub[i][1]
        if len(texto_sub[i]) == 3:
            text = text + " " + texto_sub[i][2]+"\n"
        else:
            text = text +"\n"
        arq.write(text)

    arq.close()