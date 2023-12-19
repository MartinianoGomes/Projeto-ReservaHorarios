from collections import Counter
from prettytable import PrettyTable

# Settando a tabela de Reservas
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