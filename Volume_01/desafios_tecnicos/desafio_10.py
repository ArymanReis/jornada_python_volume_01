import random
import time

preco_atual = 1000.00

print("--- ABERTURA DO MERCADO ---")

# Simula 5 segundos de pregão
for segundo in range(1, 6):
    # Sorteia variação entre -50 e +50
    variacao = random.randint(-50, 50)
    
    # Atualiza o preço
    preco_atual = preco_atual + variacao
    
    print(f"Segundo {segundo}: R$ {preco_atual:.2f} (Variação: {variacao})")
    time.sleep(1) # Espera 1 segundo real

print("--- FECHAMENTO DO MERCADO ---")