distancia = float(input("Qual a distância em km? "))
peso = float(input("Qual o peso em kg? "))
if (distancia <= 100):
    valor = peso * 1.0
elif (distancia > 100 and distancia <= 300):
    valor = peso * 1.5
elif(distancia > 300):
    valro = peso * 2.0
if(peso > 10):
    valor += 10
print(f"Valor do frete: R${valor:,.2f}")