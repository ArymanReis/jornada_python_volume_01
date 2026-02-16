print("--- CALCULADORA DE CARGA ---")

# Definição (Máquina)
def converter_sacas(qtd):
    peso_kg = qtd * 60
    return peso_kg

# Uso (Captura)
sacas_hoje = 5
peso_total = converter_sacas(sacas_hoje)

print(f"Entrada: {sacas_hoje} sacas")
print(f"Peso Total: {peso_total}kg")

# Como usamos return, podemos fazer contas com o resultado:
caminhoes = peso_total / 1000
print(f"Caminhões necessários: {caminhoes:.1f}")