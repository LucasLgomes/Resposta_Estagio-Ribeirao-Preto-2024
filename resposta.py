#1) Observe o trecho de código abaixo:

#int INDICE = 13, SOMA = 0, K = 0;

#enquanto K < INDICE faça

#{

#K = K + 1;

#SOMA = SOMA + K;

#imprimir(SOMA);



#Ao final do processamento, qual será o valor da variável SOMA?

# Definição das variáveis iniciais
INDICE = 13
SOMA = 0
K = 0

#enquanto K é menor que INDICE
while K < INDICE:
    K = K + 1  # Incrementa K
    SOMA = SOMA + K  # Adiciona o valor de K a SOMA

# Ao final do loop, imprime o valor de SOMA
print(SOMA)

#rrsultado 91

#-------------------------------------------------------------------------#

#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#preciso solicitar o usuario a escolher um numero para ter o numero que vai ser contado
numero = int(input("Informe um número para verificar na sequência de Fibonacci: "))

#dois primeiros números da sequência de Fibonacci
a, b = 0, 1
encontrado = False

# Loop para sequência de Fibonacci e verificar se o número está na sequência
while a <= numero:
    if a == numero:
        encontrado = True
    # Atualiza os valores para o próximo número da sequência
    a, b = b, a + b

# Imprime se o número está ou não na sequência de Fibonacci
if encontrado:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

#IMPORTANTE:

#Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

#-------------------------------------------------------------------------#

#3) Descubra a lógica e complete o próximo elemento:


#a) 1, 3, 5, 7, 9
    #Essa sequencia parece incrementar 2 a cada passo, Resultado 9

#b) 2, 4, 8, 16, 32, 64, 128
    #Essa sequencia parece dobrar o valor a cada passo, Resultado 128

#c) 0, 1, 4, 9, 16, 25, 36, 49
    #Parece ser os quadradros dos numeros inteiros 7^2 49

#d) 4, 16, 36, 64, 100
    #Parece ser os quadradros dos numeros pares 10^2 100

#e) 1, 1, 2, 3, 5, 8, 13
    #Sequencia de Fibonacci, 13

#f) 2,10, 12, 16, 17, 18, 19, ( resposta 20)


#-------------------------------------------------------------------------#

#4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

#Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

# 1-primeiro interruptor eu ia deixar ele ligado por alguns minutos, depois ia desligar .
#2-ia ligar o segundo interruptor e ia ate a sala das lampadas.
#3-a lampada que esta acesa e controlada pelo segundo interruptor.
# 4-eu iria tocar as lampadas restantes a que esta quente e controlada pelo primeiro interruptor, pois estava ligada por alguns minutos e depois desligada.
# 5-as restantes que está fria e apagada, e controlada pelo terceiro interruptor.


#-------------------------------------------------------------------------#

#5) Escreva um programa que inverta os caracteres de um string.

#solicita ao usuário uma string para inverter
string_original = input("Informe uma string para inverter: ")
string_invertida = ''

#inverter a string
for caractere in string_original:
    string_invertida = caractere + string_invertida

# Imprime a string invertida
print("String invertida:", string_invertida)

#IMPORTANTE:

#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

#b) Evite usar funções prontas, como, por exemplo, reverse;
