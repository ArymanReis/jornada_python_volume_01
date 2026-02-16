import math # Trazendo a caixa de ferramentas

print("--- CÁLCULO DE FRETES ---")

peso_total = 1550.0 # kg
capacidade_caminhao = 500.0 # kg

# Conta simples (divisão)
quantidade_exata = peso_total / capacidade_caminhao
print(f"Conta exata: {quantidade_exata} viagens")

# Conta real (Arredondando para CIMA)
# Ninguém faz 3.1 viagens. Tem que ser 4.
viagens_reais = math.ceil(quantidade_exata)

print("-" * 20)
print(f"Você precisa de {viagens_reais} caminhões.")