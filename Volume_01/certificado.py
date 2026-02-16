import random

def gerar_certificado(nome_aluno):
    hash_seguranca = random.randint(1000, 9999)
    print("=" * 40)
    print(f"       CERTIFICADO DE CONCLUSÃO")
    print("=" * 40)
    print("\nCertificamos que:")
    print(f"      {nome_aluno.upper()}")
    print("\nConcluiu com êxito o Módulo de")
    print("Lógica de Programação com Python")
    print("\nData: Hoje  |  Nota: 10.0")
    print(f"Código de Validação: #{hash_seguranca}")
    print("=" * 40)

nome = input("Digite seu nome completo: ")
gerar_certificado(nome)