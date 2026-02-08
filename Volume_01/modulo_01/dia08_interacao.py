# Entrada de Dados (Com Casting!)
print("--- SISTEMA DA FAZENDA ---")
fazenda = input("Nome da Fazenda: ")
sacas = int(input("Quantidade de sacas: "))
preco = float(input("Preço da saca: "))

# Processamento
faturamento = sacas * preco

# Saída
print("O faturamento da fazenda " + fazenda + " foi de:")
print(faturamento)