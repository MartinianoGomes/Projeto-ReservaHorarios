from collections import Counter
from prettytable import PrettyTable

# Settando a tabela de reservas
reservas = {
    'segunda': {'manha': {}, 'tarde': {}, 'noite': {}},
    'terca': {'manha': {}, 'tarde': {}, 'noite': {}},
    'quarta': {'manha': {}, 'tarde': {}, 'noite': {}},
    'quinta': {'manha': {}, 'tarde': {}, 'noite': {}},
    'sexta': {'manha': {}, 'tarde': {}, 'noite': {}},
}

# Exibir Tabela de Reservas
def exibir_tabela():
    dias_semana = ['segunda', 'terca', 'quarta', 'quinta', 'sexta']
    horarios_manha = ['7h30 - 8h20', '8h20 - 9h10', '9h10 - 10h00', '10h20 - 11h10', '11h10 - 12h00', '12h00 - 12h50']
    horarios_tarde = ['13h00 - 13h50', '13h50 - 14h40', '14h40 - 15h30', '15h50 - 16h40', '16h40 - 17h30', '17h30 - 18h20']
    horarios_noite = ['18h30 - 19h20', '19h20 - 20h10', '20h10 - 21h00', '21h20 - 22h00']

    for turno in ['manha', 'tarde', 'noite']:
        print(f"\nTabela de Reservas - {turno.capitalize()}: ")

        table = PrettyTable()
        table.field_names = ["Horários/Dias"] + [dia.capitalize() for dia in dias_semana]

        n = 6

        if turno == 'noite': n = 4

        for i in range(n):
            row = [f'{i+1}_{eval(f"horarios_{turno}")[i]}']

            for dia in dias_semana:
                if i+1 in reservas[dia][turno]:
                    disciplina, professor, info_adicional = reservas[dia][turno][i+1]
                    row.append(f'{disciplina} - {professor}')
                else:
                    row.append("-")

            table.add_row(row)

        print(table)

# Função para reservar os horários
def reservar_horarios(dia, turno, horario_inicio, quantidade_horas, disciplina, professor):
    for i in range(quantidade_horas):
        horario = horario_inicio + i
        if horario not in reservas[dia][turno]:
            reservas[dia][turno][horario] = (disciplina, professor, "Info Adicional")
        else:
            print(f"Horário {horario} já reservado. Escolha outro horário.")
            return False
    return True

# Verificar se a reserva existe
def verificar_reserva_existente(dia, turno, horario):
    return horario in reservas[dia][turno]

# Excluir reserva
def excluir_reserva(dia, turno, horario):
    if horario in reservas[dia][turno]:
        del reservas[dia][turno][horario]
        return True
    else:
        print(f"Não há reserva para o horário especificado.")
        return False

# Alterar reserva
def alterar_reserva(dia, turno, horario, nova_disciplina, novo_professor):
    if horario in reservas[dia][turno]:
        _, _, info_adicional = reservas[dia][turno][horario]  # Ignora a variável info_adicional
        reservas[dia][turno][horario] = (nova_disciplina, novo_professor, info_adicional)
        return True
    else:
        print("Não há reserva para o horário especificado.")
        return False

# Gerar relatório
def gerar_relatorio():
    print("\nRelatório de Reservas:\n")
    dias_semana = ['segunda', 'terca', 'quarta', 'quinta', 'sexta']
    horarios_manha = ['7h30 - 8h20', '8h20 - 9h10', '9h10 - 10h00', '10h20 - 11h10', '11h10 - 12h00', '12h00 - 12h50']
    horarios_tarde = ['13h00 - 13h50', '13h50 - 14h40', '14h40 - 15h30', '15h50 - 16h40', '16h40 - 17h30', '17h30 - 18h20']
    horarios_noite = ['18h30 - 19h20', '19h20 - 20h10', '20h10 - 21h00', '21h20 - 22h00']

    # Coleta informações para análise
    professores_counter = Counter()
    disciplinas_counter = Counter()
    dias_indisponibilidade = Counter()
    turnos_ocupacao = Counter()

    # Mostra as informações no relatório
    for turno in ['manha', 'tarde', 'noite']:
        for dia in dias_semana:
            for i in range(6):
                if i+1 in reservas[dia][turno]:
                    disciplina, professor, _ = reservas[dia][turno][i+1]
                    professores_counter[professor] += 1
                    disciplinas_counter[disciplina] += 1
                    dias_indisponibilidade[dia] += 1
                    turnos_ocupacao[turno] += 1

    print("Professores com mais horários alocados:")
    for professor, quantidade in professores_counter.most_common():
        print(f"{professor}: {quantidade} horários")

    print("\nDisciplinas que mais ocupam horários:")
    for disciplina, quantidade in disciplinas_counter.most_common():
        print(f"{disciplina}: {quantidade} horários")

    print("\nDias de maior indisponibilidade:")
    for dia, quantidade in dias_indisponibilidade.most_common():
        print(f"{dia.capitalize()}: {quantidade} horários")

    print("\nTurnos de aula com maior ocupação:")
    for turno, quantidade in turnos_ocupacao.most_common():
        print(f"{turno.capitalize()}: {quantidade} horários")

# Settando valores padrões na tabela
reservar_horarios('terca', 'manha', 1, 2, 'Economia', 'Rosiane')
reservar_horarios('quarta', 'manha', 2, 2,'Engenharia de Software', 'Zenaide')
reservar_horarios('quinta', 'manha', 4, 3,'Banco de Dados', 'Hugo')
reservar_horarios('segunda', 'tarde', 1, 3,'OAC', 'Aline Oliveira')
reservar_horarios('terca', 'tarde', 4, 2,'Estrutura de Dados', 'Léia')
reservar_horarios('sexta', 'tarde', 4, 3, 'Programação II', 'Adam')

# Função Principal
def main():
    exibir_tabela()

    # Exibindo o menu
    while True:
        opcao = input("\nEscolha uma opção:\n0 - Exibir tabela\n1 - Reservar Horário\n2 - Alterar Reserva\n3 - Excluir Reserva\n4 - Gerar Relatório\n5 - Sair\nOpção: ")

        if opcao == '0':
            exibir_tabela()

        if opcao == '1':
            n = 6

            turno = input("Escolha o turno (manha, tarde, noite): ").lower()
            while turno not in reservas['segunda']:
                turno = input("Turno inválido. Tente novamente: ")

            if turno == "noite":
                n = 4

            quantidade_horas = int(input("Digite a quantidade de horas de aula a serem reservadas: "))
            horario_inicio = int(input(f"Escolha o horário de início (1 a {n-quantidade_horas+1}): "))

            while horario_inicio < 1 or horario_inicio > n - quantidade_horas + 1:
                horario_inicio = int(input(f"Horário inválido. Escolha entre 1 e {n-quantidade_horas+1}: "))

            dia = input("Escolha o dia (segunda a sexta): ").lower()
            while dia not in reservas:
                dia = input("Dia inválido. Tente novamente: ")

            for _ in range(quantidade_horas):
                if verificar_reserva_existente(dia, turno, horario_inicio):
                    print("Pelo menos um dos horários já está reservado. Escolha outro horário.")
                    break
                horario_inicio += 1

            else:  # Executado se o loop terminar sem interrupções
                curso = input("Digite o nome do curso: ")
                periodo_curso = int(input("Digite o período do curso (numérico): "))
                disciplina = input("Digite o nome da disciplina: ")
                professor = input("Digite o nome do professor: ")

                if reservar_horarios(dia, turno, horario_inicio - quantidade_horas, quantidade_horas, disciplina, professor):
                    print(f"\nReserva feita com sucesso para {dia.capitalize()} - {turno.capitalize()}.")
                else:
                    print("\nFalha ao fazer a reserva.")

        elif opcao == '2':
            n = 6

            turno = input("Escolha o turno (manha, tarde, noite): ").lower()
            if turno not in reservas['segunda']:
                print("Turno inválido. Tente novamente.")
                continue

            if turno == "noite":
                n = 4
            horario = int(input(f"Escolha o horário (1 a {n}): "))
            while 1 < horario > n:
                horario = int(input(f"Horário inválido. Escolha entre 1 e {n}: "))

            dia = input("Escolha o dia (segunda a sexta): ").lower()
            if dia not in reservas:
                print("Dia inválido. Tente novamente.")
                continue

            nova_disciplina = input("Digite o novo nome da disciplina: ")
            novo_professor = input("Digite o novo nome do professor: ")

            if alterar_reserva(dia, turno, horario, nova_disciplina, novo_professor):
                print(f"Reserva alterada com sucesso para {dia.capitalize()} - {turno.capitalize()} - Horário {horario}.")
            else:
                print("Falha ao alterar a reserva.")

        elif opcao == '3':
            dia = input("Escolha o dia (segunda a sexta): ").lower()
            if dia not in reservas:
                print("Dia inválido. Tente novamente.")
                continue

            turno = input("Escolha o turno (manha, tarde, noite): ").lower()
            if turno not in reservas['segunda'].keys():
                print("Turno inválido. Tente novamente.")
                continue

            n = 6
            if turno == "noite":
                n = 4
            horario = int(input(f"Escolha o horário (1 a {n}): "))
            while 1 < horario > n:
                horario = int(input(f"Horário inválido. Escolha entre 1 e {n}: "))

            if excluir_reserva(dia, turno, horario):
                print(f"Reserva excluída com sucesso para {dia.capitalize()} - {turno.capitalize()} - Horário {horario}.")
            else:
                print("Falha ao excluir a reserva.")

        elif opcao == '4':
            gerar_relatorio()

        elif opcao == '5':
            print(f"\nPrograma encerrado. Obrigado!")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()