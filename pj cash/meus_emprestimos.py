coleta_de_dados_emp = {'empnc':int(input('Só uma breve confirmação de segurança\n''Número de conta: ')),
    'contaemp':int(input('Ok, agora seu número de cliente: '))}

val_emprestimos = input('''TEMOS ALGUMAS OPÇÕES DE EMPRÉSTIMO:
Escolha uma opção:
a) 1000
b) 3500
c) 5000\n''')
if val_emprestimos == 'a':
    print('Ok, seu emprestimo será liberado em aproximadamente uma semana')
if val_emprestimos == 'b':
    print('Ok, seu emprestimo será liberado em aproximadamente duas semanas úteis')
if val_emprestimos == 'c':
    print('''Ok, seu emprestimo será liberado em aproximadamente um mês
    Pode chegar antes! fique atento(a) ao seu E-mail''')