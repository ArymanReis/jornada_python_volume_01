amostra = [0, 1, 0, 0, 1, 0, 1, 0, 0]
total_defeitos = 0 # Variável contadora

# Loop For (Para cada grão na amostra...)
for grao in amostra:
    if grao == 1:
        total_defeitos = total_defeitos + 1

print(f"Foram encontrados {total_defeitos} defeitos.")