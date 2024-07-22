avaliacao = int(input("De 1 à 5, qual a sua avaliação ao filme?: "))
if(avaliacao == 1 or avaliacao == 2 or avaliacao == 3 or avaliacao == 4 or avaliacao == 5):
    if(avaliacao == 1):
        print("Ruim.")
    if(avaliacao == 2):
        print("Regular.")
    if(avaliacao == 3):
        print("Bom!")
    if(avaliacao == 4):
        print("Muito bom!")
    if(avaliacao == 5):
        print("Exelente!")
else:
    print("Inválido.")