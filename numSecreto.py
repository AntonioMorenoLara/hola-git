
NUM_SECRETO = 10;
flag = True;
while flag:
    print('Escribe un numero');
    num = int(input());
    if num > NUM_SECRETO:
        print('El numero tiene que ser menor');
    elif num < NUM_SECRETO:
        print('El numero tiene que ser mayor');
    else :
        print('Enhorabuena, has acertado');
        flag = False;