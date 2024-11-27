# Algoritmo de ordenacion - Método burbuja


def fun_ord_lis(lista):
    # Variables auxiliares
    lis_ord = lista.copy()
    seguir = True

    # Algoritmo
    while seguir:
        cont = 0
        for i in range(len(lista) - 1):
            if lista[i] <= lista[i+1]:
                lis_ord[i] = lista[i+1]
                lis_ord[i+1] = lista[i]
                cont = cont + 1
            lista = lis_ord.copy()

        if cont == 0:
            seguir = False

    print("La lista ordenada es ", lis_ord) # Salida


fun_ord_lis([5,9,3,27])
fun_ord_lis([-5,9,23,-27, 0, 15])