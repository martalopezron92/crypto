# Criptografía moderna | Marcos Ruiz
Introducción
------------

Con la **criptografía moderna** se intenta garantizar las siguientes propiedades deseables en la comunicación de información de forma segura (a estas propiedades se las conoce como funciones o servicios de seguridad):

1.  **Confidencialidad**: solamente los usuarios autorizados tienen acceso a la información.
2.  **Integridad de la información**: garantía ofrecida a los usuarios de que la información original no será alterada, ni intencional ni accidentalmente.
3.  **Autenticación de usuario**: es un proceso que permite al sistema verificar si el usuario que pretende acceder o hacer uso del sistema es quien dice ser.
4.  **Autenticación de remitente**: es el proceso que permite a un usuario certificar que el mensaje recibido fue de hecho enviado por el remitente y no por un suplantador.
5.  **Autenticación del destinatario**: es el proceso que permite garantizar la identidad del usuario destinatario.
6.  **No repudio en origen**: que cuando se reciba un mensaje, el remitente no pueda negar haber enviado dicho mensaje.
7.  **No repudio en destino**: que cuando se envía un mensaje, el destinatario no pueda negar haberlo recibido cuando le llegue.
8.  **Autenticación de actualidad (no replay)**: consiste en probar que el mensaje es actual, y que no se trata de un mensaje antiguo reenviado.

Cifrado simétrico
-----------------

La criptografía simétrica solo utiliza una clave para cifrar y descifrar el mensaje.

Esta clave la tienen que conocer el emisor y el receptor previamente.

La comunicación de las claves entre ambos sujetos es el punto débil del sistema, ya que resulta más fácil interceptar una clave que se ha transmitido sin seguridad (diciéndola en alto, mandándola por correo electrónico u ordinario o haciendo una llamada telefónica).

Los procesos de cifrar y descifrar resultan bastante **eficientes** (tardan poco tiempo en realizarse). Por esta razón, todos los algoritmos desde la antigüedad hasta los años 70, eran simétricos.

Los más utilizados actualmente son:

*   DES
*   3DES
*   AES
*   RC4
*   Blowfish
*   IDEA

![Proceso de cifrado simétrico](https://marcosruiz.github.io/assets/img/criptografia-moderna/criptografiaSimetrica.png) _Proceso de cifrado simétrico_

¿Un ejemplo de cifrado simétrico?

¿Qué ventajas/desventajas tiene el cifrado simétrico?

¿Podemos usar el mismo canal por el que nos comunicamos para enviar la clave?

¿Qué es un ataque man in the middle?

¿Por qué existe el cifrado por bloque y cifrado por flujo?

### Problemas de la criptografía simétrica

1.  **Circulación de claves**: no podemos utilizar el mismo canal inseguro por el que enviamos el mensaje. Hay que utilizar un segundo canal de comunicación, que también habría que proteger.
2.  **Gestión de claves almacenadas**: si en una empresa hay 10 trabajadores y todos tienen conversaciones privadas con todos, cada uno deberá establecer 9 contraseñas distintas y encontrar 9 canales seguros para actualizarlas. En total hay 81 claves (9 por usuario x 9 usuarios) y 81 canales… ¿O no?

El problema se puede simplificar a cuantas aristas tiene un grafo completo. Un grafo es completo si existen aristas uniendo todos los pares posibles de vértices. Es decir, todo par de vértices debe tener una arista e que los une.

\\\[{n(n-1)}/2\\\]

Siendo n el número de nodos.

En este caso n=9 por lo que…

\\\[{9(9-1)}/2 = 36\\\]

tenemos 36 aristas, que es lo mismo que 36 claves/llaves.

### Algoritmos de cifrado simétrico

En criptografía simétrica existen 2 modos de cifrado:

*   **Cifrado en bloques**: La información a cifrar se divide en bloques de longitud fija (por ejemplo 64 o 128 bits), y luego se aplica el algoritmo de cifrado a cada bloque utilizando una clave secreta. Ejemplos: DES, 3DES, AES.
*   **Cifrado de flujo**: Convierten el texto en claro en texto cifrado byte a byte. El cifrado de flujo se utiliza mucho en las telecomunicaciones. Por ejemplo, en una conversación de telefonía móvil la voz se digitaliza (es decir, se convierte a un flujo de bits) y se envía cifrada por la red de comunicaciones. Con el fin de no entorpecer la conversación, el proceso de cifrado debería ser lo bastante rápido como para no añadir retraso a la comunicación. Por ello, conviene que la operación de cifrado sea rápida. Ejemplo: RC4.

1.  Los cifrados de bloque cifran bloques de varios bytes a la vez, mientras que los cifrados de flujo lo hacen byte a byte.
2.  Los algoritmos de flujo son por su modo de funcionamiento más rápidos que los de bloque, además de tener una menor complejidad a nivel de hardware.
3.  Los algoritmos de cifrado de bloque suelen requerir de más memoria para funcionar, puesto que trabajan con bloques de datos mayores que los de flujo.
4.  Los algoritmos de cifrado de bloque son más susceptibles a la existencia de ruidos en la transmisión, lo que implica que si se interrumpe la transmisión de datos es imposible recuperarlos, mientras que los algoritmos de cifrado de flujo sí se pueden recuperar (ya que los datos son encriptados individualmente byte a byte).

A continuación vamos a describir algunos algoritmos de simétrico:

*   DES
*   3DES
*   AES
*   RC4

#### DES

El Standard de Encriptación de Datos (DES - Data Encryption Standard) es un algoritmo desarrollado a mediados de los 70s.

Se convirtió en un standard por el US National Institute of Standards and Technology (NIST), y fue adoptado por varios gobiernos en todo el mundo.

DES es un cifrado en bloque (con una longitud de 64 bits por bloque). Usa llaves de 56 bits.

Esto lo hace susceptible a una búsqueda exhaustiva de la llave con computadoras modernas y hardware de propósitos especiales.

Aunque el algoritmo DES era computacionalmente seguro, esto ha dejado de ser cierto, ya que con hardware específico es posible realizar ataques por fuerza bruta que descubran una clave en pocos días. El problema principal es que el tamaño de la clave (56 bits) es demasiado pequeño para la potencia de cálculo actual.

#### 3DES

Surge en 1999 como una versión mejorada de DES.

Cuando se descubrió que una clave de 56 bits (utilizada en el DES) no era suficiente para evitar un ataque de fuerza bruta, el 3DES fue elegido para agrandar la clave sin la necesidad de cambiar el algoritmo de cifrado.

Realiza tres veces el cifrado DES utilizando tres claves diferentes y sin relación entre ellas. Podría decirse que el Triple-DES es más fuerte que el DES simple, sin embargo, es bastante más lento comparado a algunos nuevos cifrados en bloque. Sigue siendo utilizado pero cada vez más está siendo sustituido por el algoritmo AES que ha demostrado ser muy robusto y más rápido.

![3DES](https://marcosruiz.github.io/assets/img/criptografia-moderna/3des.jpg) _3DES_

#### AES

AES (Advanced Encryption Standard o Estándar de Encriptación Avanzada) es un algoritmo de clave simétrica que remplazará el 3DES.

En Junio del 2003 el Gobierno de EEUU anunció que AES es lo suficientemente seguro para proteger la información clasificada hasta el nivel ALTO SECRETO (nivel más alto de seguridad y que se definen como información que pudiera causar “daños excepcionalmente graves” a la seguridad nacional en caso de ser divulgada al público).

El algoritmo AES posibilita tres fortalezas de clave de cifrado (contraseña de 128, 192, o 256 bits):

Cada tamaño de la clave de cifrado hace que el algoritmo se comporte ligeramente diferente

El aumento de tamaño de clave no sólo ofrece un mayor número de bits con el que se pueden cifrar los datos, sino también aumentar la complejidad del algoritmo de cifrado.

Tiempo que necesitarían los superordenadores (de alrededor de 10 PFLOPS) para descrifrar las diferentes variantes del cifrado AES

![Tiempo de descifrado de AES](https://marcosruiz.github.io/assets/img/criptografia-moderna/aesTiempoDescifrado.webp) _Tiempo de descifrado de AES_

#### RC4

El RC4 es un algoritmo de cifrado de flujo diseñado por Ronald Rivest para RSA Data Security.

Es un algoritmo de tamaño de clave variable con operaciones a nivel de byte.

Es un algoritmo de ejecución rápida en software.

El algoritmo se emplea para encriptación de ficheros y para encriptar la comunicación en protocolos como el SSL (TLS).

Cifrado asimétrico
------------------

Años 70: los criptógrafos Diffie y Hellman publicaron sus investigaciones sobre criptografía asimétrica. Su algoritmo de cifrado utiliza 2 claves matemáticas relacionadas de manera que lo que cifras con una solo lo puedes descifrar con otra.

La criptografía asimétrica se basa en el uso de dos claves:

*   La **pública**, que se podrá difundir sin ningún problema a todas las personas que necesiten mandarte algo cifrado
*   La **privada**, que no debe de ser revelada nunca.

Una VENTAJA respecto a la criptografía simétrica, ahora el emisor no necesita conocer y proteger una clave propia.

Es el receptor el que tiene el par de claves. Elige una de ellas (llamada pública) para comunicarla al emisor por si quiere enviarle algo cifrado. Pero ya no le hace falta buscar canales protegidos para eviarla porque aunque un tercer individuo la conozca, todo el que cifre con esa clave no podrá descifrarlo luego.

Lo que se cifra con la clave publica, solo puede descifrarse con la clave privada.

![Proceso de cifrado asimétrico](https://marcosruiz.github.io/assets/img/criptografia-moderna/criptografiaAsimetrica.png) _Proceso de cifrado asimétrico_

¿Qué desventajas tiene el cifrado asimétrico?

¿Con que firmamos si queremos confidencialidad?

¿Con que firmamos si queremos autenticación?

### Ventajas criptografía asimétrica

La criptografía asimétrica resuelve los 2 problemas de la clave simétrica.

1.  No necesitamos canales seguros para comunicar la clave: Podemos adjuntar la clave pública en nuestros correos, añadirla al perfil de nuestras redes sociales, en un blog… La información que nos envíen estará cifrada y solo nosotros podremos acceder a ella.
2.  No hay desbordamiento en el tratamiento de claves y canales. Si somos 9 empleados, solo necesitamos 18 claves y un canal.

### Desventajas criptografía asimétrica

Sin embargo, los algoritmos públicos presentan ciertos problemas.

1.  Poco eficientes: tardan bastante en aplicar las claves a los documentos a cifrar (Necesitan que las claves sean muy largas para asegurar la independencia matemática entre ellas). Este es el principal inconveniente de este tipo de criptografía
2.  Hay que proteger la clave privada: no bastará con dejarla en un fichero de una carpeta del disco. Las claves privadas se guardarán en un fichero (llamado keyring o llavero) y este fichero estará cifrado mediante cifrado simétrico. Es decir, para poder usar la clave privada, hay que introducir una clave que descifra el llavero y permite leerla.
3.  La necesidad de una Autoridad de Certificación (CA) en el proceso.

### Algoritmos de cifrado asimétrico

Existen varios:

*   Diffie-Hellman
*   RSA
*   DSA
*   ElGamal

#### Diffie-Hellman

La criptografía asimétrica vio su nacimiento en 1976, cuando Ralph Merkel, Whitfield Diffie y Martin Hellman crearon el primer sistema público de criptografía asimétrica. Aunque no era exactamente asimétrico, el algoritmo Diffie-Hellman supuso un primera paso importantísimo en el desarrollo de esta técnica, que pronto vio llegar más aportaciones de otros investigadores.

![Concepto del intercambio de claves secretas detrás del Diffie–Hellman](https://marcosruiz.github.io/assets/img/criptografia-moderna/intercambioDeSecreto.png) _Concepto del intercambio de claves secretas detrás del Diffie–Hellman_

#### RSA

Es un sistema criptográfico de clave pública desarrollado en 1977. Es el primer y más utilizado algoritmo de este tipo y es válido tanto para cifrar como para firmar digitalmente.

En este caso se usan dos pares de claves privadas y públicas.

Es el algoritmo de esta clase más importante y extendido.

Utiliza la exponenciación modular para cifrar y descifrar y basa su seguridad en la complejidad del problema de la factorización de enteros grandes.

Las claves pública y privada se calculan a partir de un número que se obtiene como producto de dos primos grandes. Un atacante que quiera recuperar un texto claro a partir del criptograma y de la clave pública, tiene que enfrentarse a dicho problema de factorización.

¿En qué consiste factorizar?

Garantiza no solo la confidencialidad de la comunicación entre dos partes, cifrando en origen el mensaje que se va a transmitir por un canal inseguro y descifrándolo en recepción.

También proporciona otros servicios o funciones de seguridad de la información, como son la autenticación de origen , la integridad o el no-repudio (mediante la firma digital).

#### DSA

DSA es un estándar del Gobierno Federal de los Estados Unidos de América o FIPS para firmas digitales.

#### ElGamal

El procedimiento de cifrado/descifrado ElGamal se refiere a un esquema de cifrado basado en el problema matemático del logaritmo discreto. Es un algoritmo de criptografía asimétrica basado en la idea de Diffie-Hellman y que funciona de una forma parecida a este algoritmo discreto. El algoritmo de ElGamal puede ser utilizado tanto para generar firmas digitales como para cifrar o descifrar.

Resumen del cifrado simétrico y asimétrico
------------------------------------------

El vídeo más importante…

¿Qué ventajas tiene el cifrado simétrico?

¿Qué ventajas tiene el cifrado asimétrico?

¿Se puede combinar el cifrado simétrico y asimétrico para obtener lo mejor de los dos mundos?

¿Por qué en el cifrado simétrico hay más llaves que cifrado asimétrico?

Aplicaciones reales…

¿Qué problemas tiene el cifrado simétrico?

Aún más resumido…

Criptografía híbrida
--------------------

El cifrado asimétrico no puede ser usado para cifrar todos los paquetes de intercambiados en una red local porque el bajo rendimiento del algoritmo ralentizaría el tráfico.

En su lugar se adopta un esquema híbrido (se usa criptografía asimétrica y criptografía simétrica).

1.  La criptografía asimétrica se usa para el inicio de la sesión (Hay que generar un canal seguro donde acordar la clave simétrica aleatoria que se utilizará para cifrar la conversación)
2.  La criptografía simétrica se usará durante la transmisión, utilizando la clave simétrica acordada durante el inicio de la sesión.

La clave simétrica se suele cambiar cada cierto tiempo (minutos) para dificultar más el espionaje de la conversación.

![Comunicación a través de criptografía híbrida](https://marcosruiz.github.io/assets/img/criptografia-moderna/criptografiaHibrida.png) _Comunicación a través de criptografía híbrida_

![Proceso híbrido del protocolo SSH](https://marcosruiz.github.io/assets/img/criptografia-moderna/esquemaHibridoCifradoSsh.png) _Esquema híbrido del protocolo SSH_


## Criptografía asimétrica en python

Encriptar un mensaje con la clave pública permite que sólo el que posea la clave privada equivalente pueda desencriptarlo. A continuación veremos cómo encriptar un mensaje con criptografía de curva elíptica, usando la conocida curva `secp256k1` en Python. Para ello utilizaremos la librería `ecies`, que puede ser instalada con:

Antes de nada debemos generar una `clave_privada` 🔑 y una `clave_publica` 🗝️. Lo podemos hacer de la siguiente manera. Nótese que una clave privada es simplemente un número aleatorio muy grande con mucha entropía. Aunque estuvieras años generando claves privadas, nunca encontrarías dos iguales. Podemos ver también que la `clave_publica` se deriva de la `clave_privada`.

```
from ecies import encrypt, decrypt
from ecies.utils import generate_eth_key, generate_key

eth_k = generate_eth_key()
clave_privada = eth_k.to_hex()
clave_publica = eth_k.public_key.to_hex()

print(clave_privada)
# 0x1a3d7b9a75cc2967cb2f34f276d35e60d8c72ffe9a902f2b00eb27c1ffab5ce8

print(clave_publica)
# 0x5af46da61431d3b66c3a5f5368c520c5b16ca14776c87fb6a57009befaaa9f73931dd1368a703830af31d4fdafbc23d1809717d991f18d1d2e8b5a525d3eb4a4

```

Ahora imagina que quieres comunicarte con nosotros de manera privada. Te compartimos nuestra `clave_publica`, y con ella puedes encriptar el mensaje. Ahora, el `mensage_encriptado` únicamente puede ser desencriptado por la persona que posea la `clave_privada`. En este caso, nosotros.

```
mensaje = b'Mensaje secreto para El Libro de Python'
mensage_encriptado = encrypt(clave_publica, mensaje)

print(mensage_encriptado.hex())
# 0454fad22693a4f49648e521d201d026bac7d2752d1079e255d66e12c81db529a2ad01293ca22b1249fdcd9dd0714341b7a2e5ec1961b8ee1d832f41fca8b941855badb6414dec47151f9632630c9ea7b28a195cad70d0fc2527e1870cec178f7f6fd219c01c8d03fd8f2120be3e12293e6d3563237f71bd158d2ed710a0082a50678876bfda3c75

```


Como nosotros somos los únicos que conocemos dicha `clave_privada`, podemos desencriptar el mensaje, obteniendo el mensaje en claro.

```
mensaje_desencriptado = decrypt(clave_privada, mensage_encriptado)

print(mensaje_desencriptado)
# b'Mensaje secreto para El Libro de Python'

```


Ahora imaginemos que nuestro `mensaje_encriptado` cae en malas manos. Por suerte esa persona no conoce nuestra `clave_privada` y tiene `otra_clave_privada`. Si esta persona intenta desencriptar el mensaje, obtendrá una [excepción](https://ellibrodepython.com/excepciones-try-except-finally). No podrá desencriptar el mensaje, y por lo tanto no podrá ver el contenido del mensaje.

```
otra_clave_privada = generate_key().to_hex()
mensaje_desencriptado_error = decrypt(otra_clave_privada, mensage_encriptado)

# Error: ValueError: MAC check failed

```

La magia de las matemáticas, y más en concreto, lo difícil que es factorizar números primos, protegen nuestro mensaje. Teóricamente con capacidad de computación y tiempo infinito, nuestra encriptación podría romperse, pero en la práctica es muy difícil. Al menos por ahora, mientras los ordenadores cuánticos no sean una realidad.
