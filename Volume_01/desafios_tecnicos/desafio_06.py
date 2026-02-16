pesos_sacas = [60, 59, 60, 61, 58]
peso_total = 0 # Variável acumuladora

# Loop For (Somando um por um)
for peso in pesos_sacas:
    peso_total = peso_total + peso

print(f"Carga Total: {peso_total} kg")