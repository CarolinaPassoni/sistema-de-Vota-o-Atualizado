print("=== SISTEMA DE VOTAÇÃO SIMPLIFICADO ===")

# Lista de candidatos
candidatos = [
    {"nome": "Ana", "votos": 0},
    {"nome": "Bruno", "votos": 0},
    {"nome": "Carlos", "votos": 0}
]

def mostrar_candidatos():
    for i, c in enumerate(candidatos, start=1):
        print(f"{i} - {c['nome']} ({c['votos']} votos)")

while True:
    print("\nMenu:")
    print("1 - Ver candidatos")
    print("2 - Adicionar candidato")
    print("3 - Remover candidato")
    print("4 - Votar")
    print("5 - Resultado total")
    print("0 - Sair")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        mostrar_candidatos()

    elif opcao == "2":
        nome = input("Nome do candidato: ").strip()
        if nome:
            candidatos.append({"nome": nome, "votos": 0})
            print(f"Candidato {nome} adicionado!")
        else:
            print("Nome inválido.")

    elif opcao == "3":
        mostrar_candidatos()
        entrada = input("Número ou nome do candidato para remover: ").strip()
        if entrada.isdigit():
            numero = int(entrada)
            if 1 <= numero <= len(candidatos):
                removido = candidatos.pop(numero - 1)
                print(f"Candidato {removido['nome']} removido!")
            else:
                print("Número inválido.")
        else:
            for i, c in enumerate(candidatos):
                if c['nome'].lower() == entrada.lower():
                    removido = candidatos.pop(i)
                    print(f"Candidato {removido['nome']} removido!")
                    break
            else:
                print("Candidato não encontrado.")

    elif opcao == "4":
        if not candidatos:
            print("Nenhum candidato cadastrado.")
            continue
        mostrar_candidatos()
        voto = input("Digite o número do candidato para votar: ").strip()
        if voto.isdigit() and 1 <= int(voto) <= len(candidatos):
            candidatos[int(voto)-1]["votos"] += 1
            print("Voto registrado!")
        else:
            print("Opção inválida.")

    elif opcao == "5":
        print("\n=== RESULTADO FINAL ===")
        total_votos = sum(c['votos'] for c in candidatos)
        for c in candidatos:
            print(f"{c['nome']}: {c['votos']} votos")
        print(f"Total de votos: {total_votos}")

        if total_votos > 0:
            maior_voto = max(c['votos'] for c in candidatos)
            vencedores = [c['nome'] for c in candidatos if c['votos'] == maior_voto]

            if len(vencedores) > 1:
                print(f"Empate entre: {', '.join(vencedores)} com {maior_voto} votos cada!")
            else:
                print(f"Vencedor: {vencedores[0]} com {maior_voto} votos!")
        else:
            print("Nenhum voto registrado.")

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")
