print("--- PORTARIA INTELIGENTE ---")

# Definição com Parâmetro (O Funil)
def saudacao(visitante):
    print(f"Olá, {visitante}!")
    print("Seja bem-vindo(a) à Fazenda.")
    print("-" * 15)

# Chamando com dados diferentes
saudacao("Carlos")
saudacao("Mariana")
saudacao("Pedro")

# Erro comum: Chamar vazio -> saudacao()
# O Python vai gritar: "Falta 1 argumento!"