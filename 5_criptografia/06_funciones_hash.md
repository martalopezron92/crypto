Hash
----

Un hash es un algoritmo matemático que transforma un bloque arbitrario de datos en una nueva serie de caracteres de longitud fija.

![Función hash](https://marcosruiz.github.io/assets/img/criptografia-moderna/funcionHash.png) _Función hash_

Son los siguientes:

*   SHA
*   SHA-1
*   SHA-256
*   MD5
*   RIPE-MD

Leer el artículo [¿Qué Es Un Hash Y Cómo Funciona?](https://latam.kaspersky.com/blog/que-es-un-hash-y-como-funciona/2806/)

### Características de los hash

1.  Los hashes producidos, a pesar de que son palabras parecidas, son totalmente distintos.
2.  Ambos tienen 40 caracteres de longitud: ya sean 5 caracteres los que metamos o todos los caracteres de esta presentación, la función hash hace un resumen de 40 caracteres.
3.  Son unidireccionales: no es posible, a partir del valor resumen, calcular los datos originales.
4.  No es necesario una clave para obtener el hash.
5.  No existen 2 entradas que produzcan el mismo hash.

![Ejemplos de la aplicación de un algoritmo hash](https://marcosruiz.github.io/assets/img/criptografia-moderna/ejemplosHash.png) _Ejemplos de la aplicación de un algoritmo hash_

### Aplicación de los hash

*   Almacenamiento de contraseñas: se guarda el hash que produce la contraseña pero no la contraseña.
*   Integridad de los mensajes (como ya vimos en el tema y práctica anterior).
*   Firma digital de documentos.
*   Sumas de verificación para programas: En este caso, los algoritmos generan un valor resumen a partir del código fuente que permite comprobar, por ejemplo, que la versión del programa que se ha descargado es idéntica al original y no un software malicioso.

En [esta web](https://emn178.github.io/online-tools/sha256.html).

¿Donde podemos ver los hashes de las contraseñas en un sistema GNU Linux?

¿Qué es un hash? ¿Para qué se usa?

¿Es lo mismo cifrar que aplicar una función hash?

¿Qué información hay en el fichero /etc/shadow?

 ![Salting de contraseñas](https://marcosruiz.github.io/assets/img/criptografia-moderna/saltingHashPassword.webp) _Salting de contraseñas_

### Como obtener un hash

En GNU Linux:

```
md5sum <fichero del que quiero obtener el hash>
```

En Windows:

```
winmd5 <fichero del que quiero obtener el hash>

```