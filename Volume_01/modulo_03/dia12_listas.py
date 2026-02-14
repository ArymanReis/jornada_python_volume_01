print("--- ESTOQUE INICIAL ---")
estoque = [] # Lista vazia (Vagão sem carga)
print("Estoque vazio:", estoque)

# Chegou mercadoria (Append)
estoque.append("Saca Arábica")
estoque.append("Saca Bourbon")
print("Carga carregada:", estoque)

# Venda realizada (Pop tira o último)
venda = estoque.pop()
print(f"Item vendido: {venda}")
print("Estoque atualizado:", estoque)