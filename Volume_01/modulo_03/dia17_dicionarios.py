print("--- CADASTRO DE PRODUTO ---")

# 1. Criando o dicionário
produto = {
    "tipo": "Bourbon Amarelo",
    "preco": 1500.00,
    "disponivel": True
}

# 2. Mostrando a ficha atual
print(f"Produto: {produto['tipo']}")
print(f"Valor: R${produto['preco']:.2f}")

# 3. Alteração de Mercado (Editando)
print("...Atualizando Preço...")
produto["preco"] = 1700.00

# 4. Nova Informação (Adicionando)
produto["safra"] = 2024

print("--- FICHA ATUALIZADA ---")
print(produto)