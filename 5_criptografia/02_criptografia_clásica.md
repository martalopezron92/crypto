
# Criptografía: métodos clásicos

El gran valor de la escritura, la universalización del acceso al conocimiento, es, a la vez, su gran debilidad cuando las informaciones escritas son, por unas u otras causas, de carácter confidencial.

Lo primero que inventamos para evitar que ciertos mensajes llegasen a ojos no deseados fue la **esteganografía**, consistente en ocultar el mensaje a las miradas curiosas, como cuando escribían el texto en la cabeza rapada del mensajero y esperaban a que le creciese el pelo.

Sin embargo, pronto se vio que los métodos de ocultación tenían el gran inconveniente de que una vez el engaño era descubierto el mensaje quedaba completamente expuesto. Por eso surgió la **criptografía**, "el arte de escribir con clave secreta", que consiste en ocultar no el mensaje en sí, sino el significado. De esta manera, aunque el mensaje fuese interceptado, su contenido aún estaría a salvo.

Muchos son los sistemas de encriptación. Los clásicos pueden clasificarse en **sistemas de transposición** y de **sustitución**, siendo estos últimos de dos tipos: **códigos** y **cifrados**.

## TRANSPOSICIÓN

El significado se oculta cambiando simplemente el orden de las letras del mensaje. Por ejemplo, podemos coger primero todas las letras que ocupan posiciones pares y después escribir las de las posiciones impares. De esta manera, la frase `esto es un mensaje de ejemplo` se convertiría en `SOE NMNAED JMLET SU ESJ EEEPO`.

## SUSTITUCIÓN

La idea es sustituir los elementos del texto plano (el mensaje original) por otros que formen el texto encriptado. Si lo que se sustituyen son las letras se llama **cifrado**, mientras que si lo que se sustituyen son palabras o expresiones enteras, se llama **código**.

### Cifrado César

Utilizado, de ahí su nombre, por Julio César para comunicarse con sus oficiales, consiste en sustituir cada letra del mensaje por la que está *n* posiciones más adelante o atrás en el alfabeto. Si *n* = 3, la `a` se sustituiría por la `D`, la `b` por `E`, la `c` por `F` y así sucesivamente. De este modo, la palabra `epsilones` se transforma en `HSVLÑRPHV`.

En los sistemas de encriptación se suele distinguir entre el **algoritmo** o procedimiento general y la **clave**, que sirve para singularizar el resultado del algoritmo. En el caso del cifrado César, el algoritmo sería la regla por la cual cambiamos cada carácter por uno que está *n* posiciones más adelante, mientras que la clave sería el valor concreto utilizado para *n*.

Lo malo de este sistema es que, si se sabe que se está utilizando, solo permite 27 sustituciones distintas (tantas como letras tiene el alfabeto), con lo que su descifrado es trivial. Para complicar un poco la cosa se puede utilizar, en vez de una cifra, dos, o más. Así, si la clave es 31, se sustituirá la primera letra por la que esté tres posiciones por delante, la segunda por la que esté una posición más avanzada, la tercera por la que esté tres posiciones por delante, y así sucesivamente.

El cifrado César es fácilmente matematizable: ver el Apéndice.

### Sustitución monoalfabética

A cada letra del alfabeto se le asigna un signo distinto, que puede ser otra letra o cualquier otra cosa. Por ejemplo, según la tabla siguiente, la palabra `matematicas` se transformaría en `9XD?9XD3RXM`:

| a | b | c | d | e | f | g | h | i | j | k | l | m | n | ñ | o | p | q | r | s | t | u | v | w | x | y | z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X | 5 | R | A | ? | P | 2 | U | 3 | Ñ | $ | * | 9 | E | 6 | I | W | ¿ | & | M | D | 7 | Z | T | 4 | B | @ |

Está claro que lo mejor es que la tabla sea completamente aleatoria, pero esto obliga a conocer la tabla completa. Una alternativa es la utilización de una clave para formar las equivalencias. Por ejemplo, si la clave es `EPSILON`, se escribirían a continuación el resto de las palabras del alfabeto en su orden habitual pero sin repetir las ya utilizadas. La tabla quedaría de la siguiente manera:

| a | b | c | d | e | f | g | h | i | j | k | l | m | n | ñ | o | p | q | r | s | t | u | v | w | x | y | z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E | P | S | I | L | O | N | Ñ | Q | R | T | U | V | W | X | Y | Z | A | B | C | D | F | G | H | J | K | M |

La palabra `matematicas` se cifraría como `VEDLVEDQSEC`.

### Análisis de frecuencias

Podría pensarse que tales sistemas son eficientes, pero resultan tremendamente fáciles de descifrar mediante una técnica llamada análisis de frecuencias, desarrollada primeramente por los árabes cuando estaban buscando la frecuencia con la que ciertas palabras aparecían en el Corán para dilucidar la cronología de las palabras del Profeta.

La idea fundamental es que no todas las letras aparecen con la misma frecuencia en los textos, sino que algunas aparecen más a menudo que otras. Contando las signos del texto cifrado y ordenándolos de mayor a menor frecuencia podemos establecer conjeturas acerca de qué letra corresponde a cada signo. El análisis se completa con la búsqueda de palabras frecuentes como artículos y preposiciones. Si además conocemos o sospechamos de alguna palabra que deba aparecer en el mensaje, mejor que mejor.

Para comprender en detalle cómo funciona este método en el Laboratorio se encuentra un ejemplo de descifrado por análisis de frecuencias.

Dos ejemplos de este tipo de análisis lo tenemos en los cuentos de Poe y Doyle El escarabajo de oro y La aventura de los bailarines. El cuento de Conan Doyle, en el que el criptoanalista es el mismísimo Sherlock Holmes, se caracteriza porque las letras del texto se sustituyeron por unos muñequitos danzantes.

Para evitar el análisis de frecuencias se introdujeron algunas mejoras, como la inclusión de caracteres nulos que no se traducían por nada, o la introducción de errores premeditados en el deletreado de las palabras para confundir al criptoanalista.

Una mejora importante fue el cifrado de sustitución homofónico, en el que cada letra se sustituye por varios caracteres distintos en cantidad proporcional a su frecuencia de uso, de modo que si una letra se usa el doble de veces que otra, la primera será sustituida por el doble de caracteres que la segunda. De esta manera el análisis de frecuencias queda anulado.

### Sustitución polialfabética
## Sustitución polialfabética

Leon Alberti propuso usar más de un alfabeto para encriptar cada mensaje. Vigenère desarrollaría esta idea hasta dar con un nuevo método, al que llamaron *Le chiffre indéschiffrable* (“La cifra indescifrable”). La idea es sencilla: escribimos el alfabeto una vez para cada letra empezando precisamente por esa letra. La tabla de Vigenère quedaría así:

| a | b | c | d | e | f | g | h | i | j | k | l | m | n | ñ | o | p | q | r | s | t | u | v | w | x | y | z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | B | C | D | E | F | G | H | I | J | K | L | M | N | Ñ | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| B | C | D | E | F | G | H | I | J | K | L | M | N | Ñ | O | P | Q | R | S | T | U | V | W | X | Y | Z | A |
| C | D | E | F | G | H | I | J | K | L | M | N | Ñ | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B |
| D | E | F | G | H | I | J | K | L | M | N | Ñ | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |
| E | F | G | H | I | J | K | L | M | N | Ñ | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D |
| ... | | | | | | | | | | | | | | | | | | | | | | | | | | | |

El cifrado se haría de la siguiente manera: supongamos que la clave es `CABEZA`, y que el texto a traducir es `matematicas`. Para traducir la primera letra de `matematicas`, como la primera letra de la clave es `C` utilizaremos la cuarta fila de la tabla para traducir, precisamente la que empieza por `C`, en la que vemos que a la `m` le corresponde la `Ñ`. Como la segunda letra de la clave es `A`, utilizamos para cifrar la segunda fila de la tabla, que deja la `a` como `A`. Completando el proceso, tenemos que `matematicas` se transforma en `ÑAUILAVIDER`. Obsérvese que en este sistema la misma letra puede transformarse en letras distintas.

*Le chiffre indéschiffrable* es inmune al ataque por análisis de frecuencias y fue considerada indescifrable durante mucho tiempo. Sin embargo, Charles Babbage, uno de los padres de la informática, fue capaz de romperla al encontrar que si la clave tenía *n* letras, el cifrado se repetía cada *n* letras.

---

## Claves de un solo uso

Una variación del cifrado de Vigenère consiste en utilizar una clave tan larga como el propio mensaje para evitar su carácter cíclico. Pero también se puede romper: su debilidad estriba en la utilización de claves con significado, lo que permite tener una idea de cuándo la intuición de uno va por buen camino.

La forma de resolver este problema es evidente: en vez de utilizar claves con significado hay que utilizar claves aleatorias de un solo uso. Si emisor y receptor tienen ambos un cuaderno de claves común, podrán cifrar y descifrar los mensajes utilizando las sucesivas claves contenidas en cada una de las hojas del cuaderno. Así surgió en la segunda década del siglo XX el *one time pad-cipher* ("cifrado con cuaderno de claves de un solo uso") que ofrece por primera vez un sistema absolutamente seguro.

Sin embargo, el sistema tiene dos peros importantes. Por un lado, si las necesidades criptográficas son grandes, es decir, si es mucha la cantidad de información que hay que proteger, generar claves aleatorias suficientes supone un coste muy elevado. Por otro, y este ha sido el gran problema de la criptografía a lo largo de su historia, está el problema de la **distribución de las claves**: para poder compartir un secreto, el mensaje, es necesario tener previamente un secreto compartido: la clave. Pero si aquel que no queremos que capture nuestros mensajes se hace con el cuaderno de claves será mucho peor que si no hubiésemos encriptado en absoluto, porque nosotros creeremos que estamos comunicándonos en secreto cuando no es así.


## MÁQUINAS Y ORDENADORES

Con la Segunda Guerra Mundial la criptografía se mecaniza. Máquinas como Enigma proporcionan códigos segurísimos que máquinas como la Bomba de Turing se encargan de descifrar. De hecho, una de estas máquinas, Colossus, es considerada el primer ordenador modeno.

Sin embargo, el problema central seguía siendo el mismo: la distribución de claves, o cómo transmitir la clave sin que esta sea interceptada.

Este problema hoy está resuelto con una idea genial: el uso de claves asimétricas. Pero esto es ya otra historia.

## Apéndice: las matemáticas del cifrado César

Si *x* es la posición de la letra que queremos cifrar, la posición de la nueva letra vendrá dada por la fórmula:

**f(x) = (x + n) mod p**,

donde:

- **p** = longitud del alfabeto (27 para el castellano, por ejemplo),
- **x** = número asociado a la letra (1 para la *a*, 2 para la *b*, etc.),
- **n** = clave, dependiendo de la cual cambiará el código.

Por ejemplo, si codificamos la palabra `clave` tomando *a* como la posición 1 y haciendo *n* = 5, se tiene:

- c → f(3) = (3 + 5) mod 27 = 8 → h
- l → f(12) = (12 + 5) mod 27 = 17 → p
- a → f(1) = (1 + 5) mod 27 = 6 → f
- v → f(23) = (23 + 5) mod 27 = 1 → a
- e → f(5) = (5 + 5) mod 27 = 10 → j

Para descifrar algo tan sencillo, utilizamos la fórmula inversa de aquella que hemos utilizado para cifrar (estas funciones siempre han de ser inyectivas): **f(x) = (x - n) mod p**.
