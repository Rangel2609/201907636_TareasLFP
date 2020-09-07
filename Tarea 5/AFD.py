def AFD(ingreso):
    estado = 0;
    epsilon = ''
    for compara in range(len(ingreso)):
        if estado == 0:
            if ingreso[compara] == epsilon:
                estado == 1;
                if ingreso[compara] == ['']:
                    estado == 2;
                    if ingreso[compara] == [int()]:
                        estado ==3;

        else: estado == [''];
        if estado ==0:
            if ingreso[compara] == ['']:
                estado == 1;
                if ingreso[compara] == ['']:
                    estado == 2;
                    if ingreso[compara] == [int()]:
                        estado ==3;
        break
        print("La cadena ingresada es correcta")





