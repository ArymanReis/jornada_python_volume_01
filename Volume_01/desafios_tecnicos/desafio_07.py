peso_atual = 0
capacidade_maxima = 500

# Loop While (Enquanto couber...)
while peso_atual < capacidade_maxima:
    peso_atual = peso_atual + 60 # Adiciona uma saca
    
    if peso_atual > capacidade_maxima:
        print("Silo Cheio! Parar esteira.")
        break # Para o loop imediatamente
        
    print(f"Adicionado! Peso atual no silo: {peso_atual}kg")