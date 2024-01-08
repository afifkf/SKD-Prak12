# Install Dulu Ini Bagi Yang Belum pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair
pasanganKunci = RSA.generate(2048)

kunciPublik = pasanganKunci.publickey()
print(f"Kunci publik:  (n={hex(kunciPublik.n)}, e={hex(kunciPublik.e)})")
pubKeyPEM = kunciPublik.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Kunci privat: (n={hex(kunciPublik.n)}, d={hex(pasanganKunci.d)})")
privKeyPEM = pasanganKunci.exportKey()
print(privKeyPEM.decode('ascii'))

# Get user input for the message
pesan = input("Masukkan pesan yang akan dienkripsi: ").encode('utf-8')

# Encrypt the message using the public key
enkriptor = PKCS1_OAEP.new(kunciPublik)
terenkripsi = enkriptor.encrypt(pesan)
print("Terenkripsi:", binascii.hexlify(terenkripsi))

# Decrypt the message using the private key
dekriptor = PKCS1_OAEP.new(pasanganKunci)
terdekripsi = dekriptor.decrypt(terenkripsi)
print('Terdekripsi:', terdekripsi.decode('utf-8'))