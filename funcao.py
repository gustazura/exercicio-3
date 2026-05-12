# Funções
# Para organizar o código
# Para reaproveitamento
# Primo pobre do microserviço

# Sintaxe
# def nome_funcao(parametros separados por vírgula):
#   Instruções
#   return expressao

# 1o passo é a definição da função
# 2o passo é o uso da função

print('Funções')
print('Função simples')


# 1o passo
def olamundo():
    print("Ola Mundo")


# 2o passo
olamundo()

# Função com parametros
# A gente define o parametro apenas dizendo o seu nome
# Nao precisamos definir o tipo do parametro

print('\nFunção com parametro e uso posicional')


def soma(p1, p2):
    total = p1 + p2
    print(total)


print('O total é:', end=' ')
soma(5, 6)

print('\nFunção com parametro e uso nomeado')


def subtracao(p1, p2):
    total = p1 - p2
    print(total)


print('Posicional')
print('O total é:', end=' ')
subtracao(5, 6)

print('Nomeado')
print('O total é:', end=' ')
subtracao(p2=8, p1=5)

# Escopo
# No python e em outras linguagens há uma discussão sobe escopo
# Exitem variáveis de Escopo Global e variáveis de Escopo Local
# No escopo global as variáveis são definidas no programa principal

clima = 'inverno' # O clima é de escopo global
def MostraClima():
    print(f'O clima de hoje é de {clima}')

MostrarClima()

# Percebe-se que mesmo dentro da função conseguimos acessar o valor da variável 'clima'
# A única regra que a variável global não pode esar definida depois da função

def MostraClima2():
    print(f'O clima de hoje é de{clima2}')
# Se usarmos a função antes de definir a variável global
# Ela apresenta um erro
MostraClima2()
clima2 = 'verão'
#Em outras linuages, mesmodefinindo a vaiável ates da chamada
# Da função, ela não funcionaria

clima2 = 'verão'
MostraClima()