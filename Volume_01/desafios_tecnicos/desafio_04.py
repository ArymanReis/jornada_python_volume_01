sacas = int(input("Quantas sacas deseja comprar? "))
preco_unitario = 800.00

# Lógica do Desconto
if sacas > 50:
    # Aplica 10% de desconto (multiplica por 0.90)
    total = (sacas * preco_unitario) * 0.90
    print("Desconto de Atacado aplicado!")
else:
    total = sacas * preco_unitario

print(f"Total a pagar: R$ {total:.2f}")