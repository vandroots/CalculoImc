funcionarios = [
    {
        "nome": "Paulo",
        "peso": 80,
        "altura": 1.89
    },
    {
        "nome": "Maria",
        "peso": 55,
        "altura": 1.75
    },
]


def calcula_imc(altura, peso):
    imc = peso/altura**2

    if(imc < 10):
        return "Desnutrição Grau V"
    elif(imc < 12.9):
        return "Desnutrição Grau IV"
    elif(imc < 15.9):
        return "Desnutrição Grau III"
    elif(imc < 16.9):
        return "Desnutrição Grau II"
    elif(imc < 18.4):
        return "Desnutrição Grau I"
    elif(imc < 24.9):
        return "Normal"
    elif(imc < 29.9):
        return "Pré Obesidade"
    elif(imc < 34.5):
        return "Obesidade Grau I"
    elif(imc < 39.9):
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
