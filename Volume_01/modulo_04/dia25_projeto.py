import time
import random

print("--- INICIANDO SIMULAÇÃO (5 ANOS) ---")

# 1. Função que calcula o lucro líquido
def calcular_lucro(sacas):
    preco_por_saca = 1000.00
    faturamento = sacas * preco_por_saca
    custo = faturamento * 0.30 # 30% de custo
    return faturamento - custo

# 2. Loop dos Anos
for ano in range(1, 6):
    print(f"\nANO {ano}: Plantando...")
    time.sleep(1) # Espera a natureza agir
    
    # 3. O Evento Aleatório
    evento = random.randint(1, 3)
    producao = 100 # Sacas (Base)

    if evento == 1:
        print("Evento: 🐛  PRAGA! (Produção caiu pela metade)")
        producao = producao / 2
    elif evento == 2:
        print("Evento: 🌧️  CHUVA NORMAL.")
    else:
        print("Evento: ☀️  SOL PERFEITO! (Produção dobrou)")
        producao = producao * 2
        
    lucro = calcular_lucro(producao)
    print(f"Colheita: {producao} sacas | Lucro: R${lucro:.2f}")

print("\n--- FIM DA SIMULAÇÃO ---")