def cifrado_cesar(cad_cif, clv):
    # Entrada: La cadena original cifrada (criptograma) y la clave del algoritmo
    # Salida: mensaje descifrado con la clave de entrada

    global abc
    abc = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLRMNÑOPQRSTUVWXYZ0123456789"

    # Variable auxiliar
    new_cad = "" # Cadena vacía donde se irá creando la nueva cadena descifrada

    if clv >= len(abc):
        clv = clv % len(abc)

    for i in cad_cif:
        if i in abc:
            pos = min(abc.index(i) + clv, (abc.index(i) + clv) % len(abc))
            new_cad += abc[pos]
        else:
            new_cad += " "

    return new_cad

def ejecuta():
    
    # Paso 1: Leer el contenido del archivo original
    ruta = ".//5_criptografia"
    with open(ruta + "//inputs//mensaje_original.txt", "r") as archivo_lectura:
        contenido = archivo_lectura.read()  # Leer todo el contenido

    # Paso 2: Llamamos a la función que desencriptará el mensaje
    cad_cif = cifrado_cesar(contenido, 5) # El parámetro 5 indica el numero de caracteres más frecuentes

    # Paso 3: Escribir el contenido en un archivo nuevo
    try:
        with open(ruta + "//outputs//archivo_salida_cesar.txt", "w") as archivo_escritura:
            archivo_escritura.write(cad_cif)
        print("Ejecutado correctamente. Abre el fichero 'archivo_salida.txt'")
    except:
        print("No se ha podido ejecutar correctamente")

ejecuta()


