print("--- SISTEMA DE CRACHÁS ---")
nome_sujo = input("Digite o nome do participante: ")

# Tratamento (A Limpeza)
nome_limpo = nome_sujo.strip() # Tira espaços
nome_upper = nome_limpo.upper() # Joga pra maiúsculo
tamanho = len(nome_limpo) # Conta letras

# Saída
print("-" * 20) # Truque: Multiplica o traço 20 vezes
print("NOME NO CRACHÁ:")
print(nome_upper)
print("-" * 20)
print("Total de caracteres:", tamanho)

# F-String
impresso = f"NOME DO COLABORADOR: {nome_upper} / CARGO: Especialista Em Dados Para Agronegócio"
print(impresso)