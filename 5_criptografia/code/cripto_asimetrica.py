# Descargar previamente la libreria : pip install eciespy

from ecies import encrypt, decrypt
from ecies.utils import generate_eth_key, generate_key


# Generacion claves publica y privada
eth_k = generate_eth_key()
clave_privada = eth_k.to_hex()
clave_publica = eth_k.public_key.to_hex()

print("clave publica:", clave_publica)
print("clave privada:", clave_privada)

# Cifrado con clave publica
mensaje = b'Esto es un mensaje secreto'
mensage_encriptado = encrypt(clave_publica, mensaje)
print("Mensaje encriptado:", mensage_encriptado.hex())

# Descifrado con clave privada
mensaje_desencriptado = decrypt(clave_privada, mensage_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)


# Probando a descifrar con la misma clave publica
try:
    mensaje_desencriptado = decrypt(clave_publica, mensage_encriptado)
    print("Mensaje desencriptado:", mensaje_desencriptado)
except:
    print("No es posible descifrar con la misma clave publica. Da error")

# Probando a descifrar con una clave privada generada nueva 
# (sin relacion con la publica original)
eth_k = generate_eth_key()
clave_privada = eth_k.to_hex()
clave_publica = eth_k.public_key.to_hex()

try:
    mensaje_desencriptado = decrypt(clave_publica, mensage_encriptado)
    print("Mensaje desencriptado:", mensaje_desencriptado)
except:
    print("No es posible descifrar con una clave privada distinta a la relacionada con la publica original. Da error")





