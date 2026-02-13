print("--- ALFÂNDEGA DO CAFÉ ---")
pontos = int(input("Pontuação do lote: "))
umidade = float(input("Umidade do grão (%): "))

# A Lógica Rigorosa (AND)
if pontos >= 80 and umidade < 12.0:
    print("Status: APROVADO PARA EXPORTAÇÃO 🚢")
else:
    print("Status: REPROVADO (Mercado Interno) ❌")