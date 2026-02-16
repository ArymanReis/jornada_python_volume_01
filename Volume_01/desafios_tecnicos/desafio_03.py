umidade = float(input("Digite a umidade do grão (%): "))

# Estrutura de Decisão
if umidade < 11:
    print("Resultado: Ressecado")
elif umidade <= 12:
    # Se chegou aqui, é maior que 11 e menor/igual a 12
    print("Resultado: Perfeito para Exportação")
else:
    print("Resultado: Risco de Mofo")