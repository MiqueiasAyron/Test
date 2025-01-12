#Aula007-Operadores Arimitéticos
#Ordem de precedência dos operadores: (),**,[*,/,//,%],[+,-]
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1//n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}.'.format(s, m, d), end=' ')
print('A divisão inteira {} e potência {}'.format(di, e))

#Exercício 005
n = int(input('Digite um número: '))
ns = n + 1
na = n - 1
print('O sucesso de {} é {} e o seu antecessor é {} '.format(n, ns, na))

#Exercíco 006
n = int(input('Digite um número: '))
n1 = n*2
n2 = n*3
n3 = n**0.5

print('O dobro de {} é {}, o triplo é {} e sua raiz quadrada é {}'.format(n,n1,n2,n3))