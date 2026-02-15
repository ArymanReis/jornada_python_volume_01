print("--- SELEÇÃO DE QUALIDADE ---")
sacas = [60.5, 58.0, 61.2, 59.9, 62.0]
aprovadas = 0 # Contador
total_peso = 0 # Acumulador

for peso in sacas:
    if peso > 60.0:
        print(f"Saca Aprovada: {peso}kg")
        aprovadas = aprovadas + 1
        total_peso = total_peso + peso

print("-" * 20)
print(f"Total Aprovadas: {aprovadas}")
print(f"Peso Total: {total_peso:.2f} kg")