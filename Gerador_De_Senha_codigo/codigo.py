# 1 Importar o necessário
from random import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

# 2 Pedir ao usuário o tamanho da senha
while True:
    try:
        tamanho_senha = int(input('Quantos caracteres você quer na senha? '))
    except (TypeError, ValueError):
        print('ERRO! Digite um valor inteiro')
    except KeyboardInterrupt:
        print('ERRO! O programa foi interrompido')
    else:
        print(f'CORRETO! Tamanho de senha: {tamanho_senha}')
        break

# 3 Pedir ao usuário quais caracteres podem estar na senha
opcoes_caracteres = [
    ('Deseja que a senha possa ter letras maiúsculas? (S/N): ', ascii_uppercase),
    ('Deseja que a senha possa ter letras minúsculas? (S/N): ', ascii_lowercase),
    ('Deseja que a senha possa ter números? (S/N): ', digits),
    ('Deseja que a senha possa ter símbolos? (S/N): ', punctuation)
]

caracteres_permitidos = list()

for pergunta, grupo_caractere in opcoes_caracteres:
    while True:
        try:
            resposta = str(input(pergunta)).upper()
        except KeyboardInterrupt:
            print('ERRO! O programa foi interrompido')
        else:
            if resposta not in 'SN':
                print('ERRO! Digite "S" para "Sim" ou "N" para "Não"')
            else:
                break
    if resposta == 'S':
        caracteres_permitidos.extend(grupo_caractere)


# 4 Gerar senha
senha = str()

for _ in range(0, tamanho_senha):
    senha += choice(caracteres_permitidos)

# 5 Mostrar ao usuário
print(senha)
