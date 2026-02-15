print("--- RELATÓRIO DE VENDAS ---")
vendas = [1200.00, 800.00, 450.00, 1500.00, 2000.00]

faturamento = 0
vendas_altas = 0 # Contador (> 1000)

for venda in vendas:
    # 1. Acumula
    faturamento = faturamento + venda
    
    # 2. Filtra (Alto Valor)
    if venda > 1000:
        vendas_altas = vendas_altas + 1
        print(f"⭐ Venda Destaque: R${venda:.2f}")

# 3. Média (Total dividido pelo tamanho da lista)
media = faturamento / len(vendas)

print("-" * 30)
print(f"Faturamento: R${faturamento:.2f}")
print(f"Vendas High Ticket: {vendas_altas}")
print(f"Ticket Médio: R${media:.2f}")