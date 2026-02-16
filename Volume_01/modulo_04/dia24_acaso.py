import time
import random

print("--- PREVISÃO DO TEMPO ---")

# Loop de 1 a 3 (o 4 é exclusivo)
for dia in range(1, 4):
    print(f"Analisando Dia {dia}...")
    time.sleep(1.5) # Suspense...
    
    # Sorteia: 0 ou 1
    tempo = random.randint(0, 1)
    
    if tempo == 0:
        print("Resultado: ⛈️ CHUVA")
    else:
        print("Resultado: ☀️ SOL")
        
    print("-" * 20)

print("Previsão Finalizada.")