def AFD(ingreso):
    estado = 0;
    ellipsis = ''
    for compara in range(len(ingreso)):
        if estado == 0:
            try:
                int(ingreso)
                return False
            except(True, ValueError):
                return True

        elif ingreso[compara] == ellipsis:
                 estado ==0;

        else: print("Entrada de cadena incorrecta")

        if ingreso[compara] == 1:

            ingreso[compara] = 1;
            estado == 1;

        elif ingreso[compara] == 3:
            ingreso[compara] == '';
            estado ==2;

        elif ingreso[compara] == 4:
            ingreso[compara] == '';
            estado == 3;

        elif ingreso[compara] == 5:
            ingreso[compara] == 0;
            estado ==4;
