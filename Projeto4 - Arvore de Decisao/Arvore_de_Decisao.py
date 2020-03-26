# Arvore de Decisão Simples
# link: https://estatsite.com/2016/06/11/1970/

op= int(input('Possui empréstimos em outros banco?\n1- Sim \n2- Não\n'))

if op == 1:
    ct = int(input('Trabalha de carteira assinada?\n1- Sim \n2- Não\n'))
    if ct == 1:
        cp = int(input('Possui casa própia?\n1- Sim \n2- Não\n'))
        if cp == 1:
            print('55%')
        else:
            print('40%')
    
    else:
        cp = int(input('Possui casa própia?\n1- Sim \n2- Não\n'))
        if cp == 1:
            print('40%')
        else:
            print('27%')
        
    
else:
    ct = int(input('Trabalha de carteira assinada?\n1- Sim \n2- Não\n'))
    if ct == 1:
        cp = int(input('Possui casa própia?\n1- Sim \n2- Não\n'))
        if cp == 1:
            print('80%')
        else:
            print('75%')
    
    else:
        cp = int(input('Possui casa própia?\n1- Sim \n2- Não\n'))
        if cp == 1:
            print('70%')
        else:
            print('60%')
    

