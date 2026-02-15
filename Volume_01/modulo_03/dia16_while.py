print("--- INICIANDO TORRA ---")
temperatura = 0 # Estado inicial

# ENQUANTO não atingir 200 graus...
while temperatura < 200:
    print(f"Temperatura atual: {temperatura}°C")
    temperatura = temperatura + 50 # Aquece

print("-" * 20)
print(f"PRONTO! Temperatura final: {temperatura}°C")
print("Torra finalizada.")