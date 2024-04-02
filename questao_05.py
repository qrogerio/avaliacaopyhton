numero_mes = int(input("Digite um número de 1 a 12: "))
def mes_correspondente(numero):
    match numero:
        case 1:
            return "Janeiro"
        case 2:
            return "Fevereiro"
        case 3:
            return "Março"
        case 4:
            return "Abril"
        case 5:
            return "Maio"
        case 6:
            return "Junho"
        case 7:
            return "Julho"
        case 8:
            return "Agosto"
        case 9:
            return "Setembro"
        case 10:
            return "Outubro"
        case 11:
            return "Novembro"
        case 12:
            return "Dezembro"
        case _:
            return "Número inválido. Digite um valor entre 1 e 12."
        
print(f"O mês correspondente ao número {numero_mes} é {mes_correspondente(numero_mes)}.")
