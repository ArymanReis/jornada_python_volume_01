print("--- LOJA DE PEÇAS ---")

imposto_federal = 0.20 # Variável GLOBAL (Visível a todos)

def calcular_preco(custo):
    lucro = 50.00 # Variável LOCAL (Só existe aqui)
    final = custo + lucro + (custo * imposto_federal)
    return final

peca = 100.00
preco_venda = calcular_preco(peca)

print(f"Preço de Venda: R${preco_venda:.2f}")

# TENTE DESCOMENTAR A LINHA ABAIXO:
# print(lucro) 
# Erro: NameError (O Python não acha a variável 'lucro')