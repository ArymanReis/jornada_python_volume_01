print("--- BALANÇA DA FAZENDA ---")
pesos = [60.5, 59.0, 61.2, 60.0]
total_peso = 0 # Nosso acumulador começa zerado

# O Loop (A Esteira)
for peso_atual in pesos:
    print(f"Processando saca de: {peso_atual}kg")
    total_peso = total_peso + peso_atual

# Saída (Fora do loop, recuado para a esquerda)
print("-" * 20)
print(f"Peso Total: {total_peso} kg")