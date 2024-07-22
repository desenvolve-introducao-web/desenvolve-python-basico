comprimento = int(input("Digíte o comprimento do terreno em metros: "))
largura = int(input("Digíte a largura do terreno em metros: "))
preço_m2 = float(input("Digíte o preço do metro quadrado da região: "))
area = comprimento * largura
preço = area * preço_m2
print(f"O terreno possui {area}m2 e custa R${preço:,.2f}.")