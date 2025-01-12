n = (input('Digite qualquer coisa: '))
if n.isnumeric():
    print('O valor de entrada é numérico')
elif n.isalpha():
    print('O valor da entrada é alfabético')
elif n.isalnum():
    print('O valor da entrada é alfanumérico')