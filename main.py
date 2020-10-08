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

x = PrettyTable(["Bases", "Operador 1", "op","Operador 2", "=","Resultado"])
x.set_style(PLAIN_COLUMNS)


# Alinha as colunas
""" x.align["Hexadecimal"] = "l"
x.align["UF"] = "l"
x.align["População"] = "r"
x.align["IDH-M"] = "r"
x.align["Renda per Capita"] = "r" """

caracteres = ["+", "-", "*", "/", "|", "&"]


def calculo(op1,op2,operacao):
    resultado = None
    op1 = int(op1)
    op2 = int(op2)
    

    if operacao == "+":
        resultado = op1 + op2

    if operacao == "-":
        resultado = op1 - op2

    if operacao == "*":
        resultado = op1 * op2

    if operacao == "/":
        resultado = op1 / op2

    if operacao == "|":
        resultado = op1 | op2

    if operacao == "&":
        resultado = op1 & op2

    
    return resultado

def buscaOperacao(expressao):
    global caracteres
    for caractere in caracteres:
        if caractere in entrada:
            return caractere
    return False

def formataBases(decimal):
    lista_bases = []
    lista_bases.append("{:02x}".format(decimal))
    lista_bases.append(decimal)
    lista_bases.append("{:02o}".format(decimal))
    lista_bases.append("{:02b}".format(decimal))

    return lista_bases


entrada = input("Digite a expressão")
operacao = buscaOperacao(entrada)


if operacao != False:
    hexadecimal = ['Hexadecimal']
    decimal = ['Decimal']
    octal = ['Octal']
    binario = ['Binário']

    operadores = entrada.split(operacao)
    resultado = calculo(operadores[0],operadores[1],operacao)
    
    bases_op0 = formataBases(int(operadores[0]))
    bases_op1 = formataBases(int(operadores[1]))
    bases_res = formataBases(resultado)

    hexadecimal.append(bases_op0[0])
    hexadecimal.append(operacao)
    hexadecimal.append(bases_op1[0])
    hexadecimal.append('=')
    hexadecimal.append(bases_res[0])
    
    decimal.append(bases_op0[1])
    decimal.append(operacao)
    decimal.append(bases_op1[1])
    decimal.append('=')
    decimal.append(bases_res[1])
    
    octal.append(bases_op0[2])
    octal.append(operacao)
    octal.append(bases_op1[2])
    octal.append('=')
    octal.append(bases_res[2])

    binario.append(bases_op0[3])
    binario.append(operacao)
    binario.append(bases_op1[3])
    binario.append('=')
    binario.append(bases_res[3])
     
    x.add_row(hexadecimal)
    x.add_row(decimal)
    x.add_row(octal)
    x.add_row(binario)

    print(x)

else:
   print("Não há nada a se fazer")
