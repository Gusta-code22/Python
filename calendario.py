import calendar

# Imprime o calendário de janeiro de 2024
print(calendar.month(2024, 1))

# Loop para imprimir os calendários de fevereiro a dezembro, com uma linha em branco entre cada mês
for i in range(2, 13):
    print(calendar.month(2024, i))
    print()  # Adiciona uma linha em branco

import calendar

# Função para gerar e exibir o calendário do ano inteiro
def print_year_calendar(year):
    # Cria uma instância de TextCalendar
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    # Cabeçalho
    print(f"Calendário Completo - {year}")
    print()
    
    # Imprime o calendário de cada mês do ano
    for month in range(1, 13):
        print(cal.formatmonth(year, month))
        print('-' * 20)  # Linha separadora para melhorar a visualização

# Chama a função para imprimir o calendário de 2024
print_year_calendar(2024)
