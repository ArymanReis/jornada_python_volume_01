# Definição da Função (A Máquina)
def converter_para_libras(peso_kg):
    resultado = peso_kg * 2.2
    return resultado # Entrega o valor calculado

# Uso da Função
peso_entrada = 50
peso_convertido = converter_para_libras(peso_entrada)

print(f"{peso_entrada}kg equivalem a {peso_convertido:.1f} lbs")