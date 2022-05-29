# Validação de Dados - Só aceitar Masculino e Feminino - Errado: Pedir para digitar até chegar em um valor correto
sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("Dados inválidos! Digite novamente: "))
print(f"Sexo {sexo} registrado com sucesso!")
    
