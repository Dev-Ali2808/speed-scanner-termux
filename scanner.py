import os

def auditor(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print("Arquivo de teste nao encontrado!")
        return

    print("-" * 35)
    print("AUDITOR SPED - ADS & CONTABILIDADE")
    print("-" * 35)

    with open(nome_arquivo, 'r', encoding='latin-1') as f:
        linhas = f.readlines()

    erros = 0
    for i, linha in enumerate(linhas, 1):
        # Regra simples: linha deve começar e terminar com pipe |
        if not (linha.startswith('|') and linha.strip().endswith('|')):
            print(f"Erro na linha {i}: Layout invalido (falta pipe).")
            erros += 1

    if erros == 0:
        print("✅ Arquivo OK! Estrutura validada.")
    else:
        print(f"❌ Fim do scan. Total de erros: {erros}")

# Chama a função para testar o arquivo que vamos criar a seguir
auditor("teste.txt")
