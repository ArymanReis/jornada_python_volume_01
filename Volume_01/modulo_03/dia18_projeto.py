print("--- SISTEMA DE GESTÃO ---")

# Lista de Dicionários (O Caminhão)
safra = [
    {"grao": "Arábica", "valor": 1200.00},
    {"grao": "Robusta", "valor": 800.00},
    {"grao": "Arábica", "valor": 1150.00}
]

faturamento = 0 # Acumulador

# Para cada saca (dicionário) na lista...
for saca in safra:
    print(f"Processando: {saca['grao']}")
    # Somamos apenas a chave "valor"
    faturamento = faturamento + saca["valor"]

print("-" * 25)
print(f"Total Safra: R${faturamento:.2f}")