# This is an AES 128 implementation
#import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
 
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
#password = input("Enter encryption password: ")
 
 
def get_private_key(password):
    salt = b"this is a salt"
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:16]
    return key
 
 
def encrypt(raw, private_key,iv):#password):
    #private_key = get_private_key(password)
    raw = pad(raw)
    #iv = Random.new().read(AES.block_size)
    #iv = hashlib.sha256(private_key+
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    #return base64.b64encode(iv + cipher.encrypt(raw))
    return cipher.encrypt(raw)
    #return base64.b64encode(cipher.encrypt(raw))
 
 
def decrypt(raw,private_key,iv):
    #private_key = get_private_key(password)
    #raw = base64.b64decode(raw)
    #iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    #return unpad(cipher.decrypt(enc[16:]))
    return unpad(cipher.decrypt(raw))
 
'''
encrypted = encrypt("hello there how are you doing", password)
print(encrypted)
 

decrypted = decrypt(encrypted, password)
print(bytes.decode(decrypted))'''
