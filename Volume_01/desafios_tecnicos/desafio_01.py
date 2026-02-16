# Dados do problema
faturamento = 1000.00
custo = 450.00

# Lógica
lucro_liquido = faturamento - custo
por_socio = lucro_liquido / 2

# Saída formatada
print(f"Lucro Total: R$ {lucro_liquido:.2f}")
print(f"Parte por Sócio: R$ {por_socio:.2f}")