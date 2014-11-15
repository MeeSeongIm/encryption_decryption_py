
#
#
# using elliptic curve cryptography to encrypt messages. 
#
# use with seccure: https://github.com/MeeSeongIm/py-seccure
#
#



import seccure

str(seccure.passphrase_to_pubkey(b'my private key'))  # devive the public key 

ciphertext = seccure.encrypt(b'This is a secret message.\n', b'8W;>i^H0qi|J&$coR5MFpR*Vn')

print(ciphertext)

seccure.decrypt(ciphertext, b'my private key')

seccure.sign(b'This will be a signed message.\n', b'my private key') 

seccure.verify(b'This will be a signed message.\n', b'', b'8W;>i^H0qi|J&$coR5MFpR*Vn')  # to verify the signature

