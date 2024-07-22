ano = int(input("Insira o ano: "))
if(ano % 4 == 0 and (not ano % 100 == 0) or ano % 400 == 0):
    print(f"{ano} é um ano Bissexto.")
else:
    print(f"{ano} não é um ano Bissexto.")