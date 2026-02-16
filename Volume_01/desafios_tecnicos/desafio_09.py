producao = [1200, 1500, 1100, 1800, 1300]

# Passo 1: Assumimos que o primeiro é o maior por enquanto
recorde = 0 

# Passo 2: Verificamos todos os anos
for ano in producao:
    if ano > recorde:
        recorde = ano # Atualizamos o recorde se encontrarmos um maior

print(f"O recorde de produção foi: {recorde} sacas")