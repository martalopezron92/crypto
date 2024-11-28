
Firma electrónica
-----------------

La firma electrónica es un conjunto de datos electrónicos que acompañan o que están asociados a un documento electrónico y cuyas funciones básicas son:

*   **Identificar al firmante de manera inequívoca**.
*   **Asegurar la integridad del documento firmado**. Asegura que el documento firmado es exactamente el mismo que el original y que no ha sufrido alteración o manipulación.
*   **Asegurar el no repudio del documento firmado**. Los datos que utiliza el firmante para realizar la firma son únicos y exclusivos y, por tanto, posteriormente, no puede decir que no ha firmado el documento.

Generalmente, la ley equipara la firma electrónica a la firma manuscrita.

Podemos precisar varios tipos:

*   Firma electrónica **simple**: contempla los datos electrónicos empleados por la persona firmante. Es la que posee un menor nivel de seguridad. Por ejemplo: firma digitalizada.
*   Firma electrónica **avanzada**: permite, además de conocer a la persona firmante, saber si se han efectuado cambios posteriormente. Por ejemplo: firma digital.
*   Firma electrónica **cualificada**: se trata de una firma electrónica avanzada que ha sido generada por un dispositivo capacitado para la creación de firmas electrónicas. Por ejemplo: firma digital.

### Proceso básico de firma electrónica

El proceso básico que se sigue para la firma electrónica es el siguiente:

1.  El usuario dispone de un documento electrónico (una hoja de cálculo, un pdf, una imagen, incluso un formulario en una página web) y de un certificado que le pertenece y le identifica.
2.  La aplicación o dispositivo digital utilizados para la firma realiza un resumen del documento. El resumen de un documento de gran tamaño puede llegar a ser tan solo de unas líneas. Este resumen es único y cualquier modificación del documento implica también una modificación del resumen.
3.  La aplicación utiliza la clave privada para codificar el resumen.
4.  La aplicación crea otro documento electrónico que contiene ese resumen codificado. Este nuevo documento es la firma electrónica.

Firma digital
-------------

*   La primera utilidad de la criptografía es **ocultar el mensaje** o encriptarlo, es decir, garantizar la confidencialidad de la comunicación.
*   La segunda es conseguir **determinar la autenticidad del emisor**. ¿Cómo podría estar seguro un general romano de que el mensaje con las órdenes venía de otro general romano y no del algún enemigo? Si el enemigo conocía el algoritmo de cifrado y la clave actual, podía intentar engañarle mediante un mensaje falso pero correctamente cifrado.
*   La tercera utilidad es **asegurar el no repudio** del documento firmado (firma).

La **firma electrónica** es por tanto un conjunto de datos electrónicos que acompañan a una determinada información también en formato electrónico. Realizar una firma electrónica quiere decir que una persona física verifica una acción o procedimiento mediante un medio electrónico, dejando un registro de la fecha y hora de la misma.

Una **firma digital** es una implementación técnica específica de algunas firmas electrónicas mediante la aplicación de algoritmos criptográficos. Por tanto, se refieren a la tecnología de cifrado / descifrado en la que se basan algunas firmas electrónicas como la avanzada y cualificada.

![Firma electrónica vs firma digital](https://marcosruiz.github.io/assets/img/criptografia-moderna/firmaElectronicaVsFirmaDigital.png) _Firma electrónica vs firma digital_

La firma digitalizada es la conversión del trazo de una firma en una imagen. Para obtener tu propia firma digitalizada tienes que realizarla sobre un papel y escanearla. O bien realizarla mediante algún tipo de hardware, como pueden ser los pads de firma, que te permiten guardar la imagen de tu firma en el ordenador - en formato .jpg o .png - y utilizarla cada vez que la necesites.

La firma digitalizada se considera firma electrónica simple, con lo cual es legal. Pero no ofrecen ninguna garantía respecto a la identidad del firmante (que es una característica de las firmas simples).

Además, las firmas digitalizadas se pueden falsificar muy fácilmente. Con lo que resulta paradójico que este tipo de firmas sea de las más utilizadas por la mayoría de las personas para firmar, y dar su consentimiento, en muchos documentos y contratos.

### Proceso de firma digital

![Proceso de firma digital](https://marcosruiz.github.io/assets/img/criptografia-moderna/procesoFirmaDigital.png) _Proceso de firma digital_

![Proceso de firma digital](https://marcosruiz.github.io/assets/img/criptografia-moderna/firmaDigital.png) _Proceso de firma digital_

#### Paso 1

El emisor aplica al documento una función de resumen (Función hash).

El resultado de esa función es un lista de caracteres (resumen), que la función garantiza que solo se puede haber obtenido con el documento original

El algoritmo de la función hash no necesita una clave externa como los algoritmos de cifrado

#### Paso 2

Ahora el emisor cifra ese resumen con su clave privada y lo envía al destinatario junto con el documento original.

#### Paso 3

En el destino se hacen 2 operaciones:

1.  Aplicar la misma función hash al documento para obtener su resumen.
2.  Descifrar el resumen recibido, utilizando la clave publica del emisor.

Si ambos resúmenes coinciden, el destino puede estar seguro que el emisor del documento es el mismo que el dueño de la clave pública.

Por supuesto, si queremos que el documento original no pueda ser interceptado en la transmisión (emisor -> receptor), deberemos cifrarlo.

Certificado digital de clave pública
------------------------------------

Es, principalmente, un documento digital que contiene nuestros datos identificativos que están autentificados por un organismo oficial. El certificado digital es un documento que confirma nuestra identidad en internet como Persona Física y es obligatorio para poder consultar y realizar trámites con la Administración Pública.

![Certificado digital](https://marcosruiz.github.io/assets/img/criptografia-moderna/certificadoDigital.png) _Certificado digital_

![Captura de pantalla de un certificado digital](https://marcosruiz.github.io/assets/img/criptografia-moderna/screenshotCertificadoDigital.png) _Captura de pantalla de un certificado digital_

¿Se puede validar un certificado sin conexión a Internet?

¿Qué es una lista de revocación de certificados?

PKI (Public Key Infraestructure)
--------------------------------

Hasta de ahora hemos aprendido…

*   Enviar documentos a un destinatario de manera que solo él podría leerlos (cifrado)
*   Identificar al firmante
*   Asegurar la integridad del documento firmado y asegurar el no repudio del documento firmado (firma)

En todos los casos necesitaríamos una comprobación extra sobre la clave pública: comprobar que la huella de la clave importada coincide con la huella de la clave original (Para asegurarnos de que vamos a comunicarnos con la persona correcta - AUTENTIFICACIÓN).

Comprobación de la huella con gpg:

La PKI o Public Key Infrastructure es la tecnología tras los certificados digitales. Al igual que un permiso de conducir o un pasaporte, un certificado digital demuestra su identidad y le otorga ciertos permisos. Un certificado digital permite que su propietario cifre, firme y autentique. Por tanto, PKI es la tecnología que le permite cifrar datos, firmar documentos y autenticarse mediante certificados.

Con el PKI se asegura:

*   **Integridad**: El mensaje no ha sido cambiado.
*   **No repudio**: La capacidad de demostrar o probar la participación de las partes
*   **Identificación**: Mecanismo o proceso que provee la capacidad de identificar a un usuario de un sistema.
*   **Autenticación**: Permite verificar la identidad o asegurar que un usuario es quien dice ser.

¿Se puede usar cifrado simétrico para realizar una firma electrónica?

¿Qué es el no repudio?

### Nuevos interlocutores

*   **Autoridad de Certificación (CA)**: su misión es emitir certificados. Hasta ahora los generábamos nosotros mismos.
*   **Autoridad de Registro (RA)**: es la responsable de asegurar que el solicitante del certificado es quien dice ser.
*   **Autoridad de Validación (VA)**: es la responsable de comprobar la validez de los certificados digitales emitidos. Suele coincidir con la CA.

![Interlocutores PKI](https://marcosruiz.github.io/assets/img/criptografia-moderna/pki.jpg) _Interlocutores PKI_

### Funcionamiento PKI

1.  Durante el inicio de la sesión, el SERVIDOR envía su clave publica al CLIENTE. El CLIENTE, antes de iniciar el diálogo, DESCONFIA (necesita comprobar que el servidor es quien dice ser).
2.  El SERVIDOR lo ha supuesto y ha enviado, junto con su clave pública, la firma digital de esa clave. Esa firma digital ha sido realizada por una CA oficial (utilizando la clave privada de esa CA)
3.  El CLIENTE puede verificar la firma recibida utilizando la clave pública de la CA. Si la firma es correcta, la clave pública del SERVIDOR también lo es y podemos iniciar una sesión segura con toda confianza.

Por lo tanto, para que funcione la autentificación de clave publica mediante PKI, se necesitan 2 pasos previos:

*   El SERVIDOR ha conseguido que una CA firme su clave publica (Por ejemplo, Verisign, FNMT…)
*   El CLIENTE dispone de la clave pública de esa CA dentro de su llavero de claves asimétricas.


## Firma digital en Python

A continuación veremos cómo crear una firma digital usando Python. Para ello firmamos un mensaje con nuestra clave privada, lo que permite que cualquiera pueda verificar que nosotros hemos creado dicho mensaje, haciendo uso de nuestra clave pública. Usaremos la librería `cryptography`:

Antes de nada necesitamos crear una `clave_privada` 🔑 y derivar de ella la `clave_publica` 🗝️. Similar al ejemplo anterior, pero en este caso usamos otra librería.

```
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature

# generamos una clave privada y derivamos la pública
clave_privada = ec.generate_private_key(ec.SECP256R1())
clave_publica = clave_privada.public_key()

```
Si tienes curiosidad de ver que pinta tiene la clave privada, la puedes imprimir de la siguiente manera. Existen diferentes formatos para representarla. Y recuerda, si la usas en casos reales, jamás la compartas con nadie.

```
from cryptography.hazmat.primitives import serialization

pem = clave_privada.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

print(pem)

```

Ahora viene lo importante. Usando `sign`, podemos crear nuestra firma digital. Como podemos ver, únicamente necesitamos nuestra clave privada y el mensaje a firmar. El `SHA256` es simplemente la función [hash](https://ellibrodepython.com/hash-python) utilizada para “resumir” nuestro mensaje. Es decir, lo que realmente se firma no es el mensaje entero, sino el hash del mismo, en este caso el `SHA256` del mensaje. Esto es más eficiente, ya que el hash tiene un tamaño fijo y posiblemente menor que el mensaje. Y la gran ventaja es que este hash, representa de manera unívoca a el mensaje.

```
firma = clave_privada.sign(
    b"Envía 1 € a la dirección 0x1234",
    ec.ECDSA(hashes.SHA256())
)

print(firma.hex())
# 304502205abea2fb8d3be8a8b9caddd175ebd67edb38fbae051c618134eb5b529e17af1e022100a75540b213806e3d831f785246c7caf0ad171ff220fda356aa248e54583b1d93

```


Una vez tenemos la firma, podemos enviársela a cualquier persona junto con el mensaje. Por ejemplo, esta firma y mensaje podrían ser una transacción en la blockchain. Esta actúa como una firma manuscrita, donde se garantiza que el creador conocía la `clave_privada`.

Ahora, un tercero podría verificar que el mensaje fue efectivamente creado por el conocedor de `clave_privada`. Para esto sólo se necesita `clave_publica`. Una clave pública que cualquiera puede conocer.

```
clave_publica.verify(
        firma,
        b"Envia 1 euro a la direccion 0x1234",
        ec.ECDSA(hashes.SHA256())
)

```
Imaginemos que alguien ha interceptado la comunicación y ha alterado el mensaje, cambiando la dirección. En vez de solicitar 1 euro a `0x1234` se solicita a `0x5678`. Si esto fuera una aplicación real, alguien podría engañar al receptor y hacerle enviar fondos a una dirección distinta.

Sin embargo, si intentamos verificar la firma con `verify` podemos ver obtendremos una excepción `InvalidSignature`. Es decir, la firma no es válida, ya que el mensaje se ha visto alterado. Nos hemos protegido de un atacante modificando el mensaje.

```
clave_publica.verify(
        firma,
        b"Envia 1 euro a la direccion 0x5678",
        ec.ECDSA(hashes.SHA256())
)
# Error: cryptography.exceptions.InvalidSignature

```

No olvides capturar la excepción como explicamos [aquí](https://ellibrodepython.com/excepciones-try-except-finally). Es importante notar lo mismo pasa si la firma se cambia o si la clave pública que estamos usando no corresponde con la privada que creó la firma original. La firma digital asegura la integridad del mensaje.
