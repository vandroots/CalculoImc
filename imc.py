"""
1.	Uma empresa, preocupada com a saúde de seus funcionários decidiu fazer um 
acompanhamento médico de peso. Suponha a existência de uma lista de dicionários 
contendo as informações médicas dos funcionários como o modelo abaixo:

[
    {
        "nome":"José",
        "peso":80,
        "altura":1.89
    },
    {
        "nome":"Maria",
        "peso":55,
        "altura":1.75
    },
]

O algoritmo deve, com as informações do peso e da altura, 
checar a situação de cada funcionário da lista e imprimir a situação conforme a tabela abaixo:

"""

funcionarios = [
    {
        "nome":"José",
        "peso":80,
        "altura":1.89
    },
    {
        "nome":"Maria",
        "peso":55,
        "altura":1.75
    },
]

def calcula_imc(altura,peso):
    imc = peso/altura**2

    if(imc<10):
        return "Desnutrição Grau V"
    elif(imc<12.9):
        return "Desnutrição Grau IV"
    elif(imc<15.9):
        return "Desnutrição Grau III"
    elif(imc<16.9):
        return "Desnutrição Grau II"
    elif(imc<18.4):
        return "Desnutrição Grau I"
    elif(imc<24.9):
        return "Normal"
    elif(imc<29.9):
        return "Pré Obesidade"
    elif(imc<34.5):
        return "Obesidade Grau I"
    elif(imc<39.9):
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

for funcionario in funcionarios:
    situcao = calcula_imc(funcionario["altura"], funcionario["peso"])
    print("Nome: "+funcionario["nome"])
    print("Peso: "+str(funcionario["peso"]))
    print("Altura: "+str(funcionario["altura"]))
    print("Situação: "+situcao)
    print("--------------------------------------------------------")
    