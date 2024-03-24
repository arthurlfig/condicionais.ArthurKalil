uni = input("Em qual universidade vc estuda?")
n1 = float(input(" digite sua primeira nota"))
n2 = float(input(" digite sua segunda nota"))
media = (n1 + n2) / 2
if uni =="pucpr" and media >= 7:
    print("Aprovado!!!")
elif uni == "pucpr" and media < 7 and media >= 4:
    print("recuperação")
elif uni == "pucpr" and media < 4:
    print("Reprovado")
elif uni == "Unicamp" and media >= 5:
    print("Aprovado!!")
elif uni == "Unicamp" and media < 5:
    print("recuperação")