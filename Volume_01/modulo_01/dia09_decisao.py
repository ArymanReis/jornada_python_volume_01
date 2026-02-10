print("--- ROBÔ DE CLASSIFICAÇÃO ---")
pontos = int(input("Digite a pontuação do café (0-100): "))

if pontos >= 80:
  print("Resultado: CAFÉ ESPECIAL (Ouro)")
elif pontos >= 60:
  print("Resultado: CAFÉ SUPERIOR (Prata)")
else:
  print("Resultado: CAFÉ TRADICIONAL (Bronze)")

print("Análise finalizada.")