from prettytable import PrettyTable
from prettytable import PLAIN_COLUMNS

""" 
SAÍDA PARA CALCULOS SIMPLES: 
    print("bin| 1100 + 0011 = 1111")
    print("dec| 12   + 3    = 15")
    print("hex| C    + 3    = F")
    print("oct| 1100 + 0011 = 1111")
    print("asc| -    + -    = -")
"""

table = PrettyTable(["Bases", "Operador 1", "op",
                     "Operador 2", "=", "Resultado"])


# Alinha as colunas
""" table.align["Hexadecimal"] = "l"
table.align["UF"] = "l"
table.align["População"] = "r"
table.align["IDH-M"] = "r"
table.align["Renda per Capita"] = "r" """

caracteres = ["+", "-", "*", "/", "|", "&"]


def calculation(op1, op2, operation):
    result = None
    op1 = int(op1)
    op2 = int(op2)

    if operation == "+":
        result = op1 + op2

    if operation == "-":
        result = op1 - op2

    if operation == "*":
        result = op1 * op2

    if operation == "/":
        result = op1 / op2

    if operation == "|":
        result = op1 | op2

    if operation == "&":
        result = op1 & op2

    return result


def findOperation(expression):
    global caracteres
    for caractere in caracteres:
        if caractere in expression:
            return caractere
    return False


def formataBases(decimal):
    list_bases = []
    list_bases.append("{:01x}".format(decimal))
    list_bases.append("{:01d}".format(decimal))
    list_bases.append("{:01o}".format(decimal))
    list_bases.append("{:01b}".format(decimal))

    return list_bases


while True:
    expression = input("Digite a expressão: \n")
    operation = findOperation(expression)

    if operation != False:
        hexadecimal = ['Hexadecimal']
        decimal = ['Decimal']
        octal = ['Octal']
        binary = ['Binário']
        list_rows = [hexadecimal, decimal, octal, binary]

        operators = expression.split(operation)
        result = calculation(operators[0], operators[1], operation)

        bases_op0 = formataBases(int(operators[0]))
        bases_op1 = formataBases(int(operators[1]))
        bases_res = formataBases(int(result))

        for row in range(len(list_rows)):
            list_rows[row].append(bases_op0[row])
            list_rows[row].append(operation)
            list_rows[row].append(bases_op1[row])
            list_rows[row].append('=')
            list_rows[row].append(bases_res[row])

        table.add_row(hexadecimal)
        table.add_row(decimal)
        table.add_row(octal)
        table.add_row(binary)

        print(table)

        table.clear_rows()

    else:
        print("Não há nada a se fazer")
