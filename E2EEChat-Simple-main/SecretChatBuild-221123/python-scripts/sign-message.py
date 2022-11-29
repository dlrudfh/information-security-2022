from Crypto import Random
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import base64

def decode_base64(b64):
    return base64.b64decode(b64)

def encode_base64(p):
    return base64.b64encode(p).decode('ascii')

def make_message_hash(msg):
    return SHA256.new(msg.encode('utf-8'))

def read_from_base64():
    return [ input(), decode_base64(input()) ]

def sign(msg, key):
    return pkcs1_15.new(key),sign(make_message_hash(msg))

[msg, prikey] = read_from_base64()

sign_result = sign(msg, prikey)
print( encode_base64(sign_result) )