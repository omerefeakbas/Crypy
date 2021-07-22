import crypt
from os import pread

messageEncoded = crypt.encode_ascii("Expample Message","expamplepassword")
messageDecoded = crypt.decode_ascii(messageEncoded,"expamplepassword")
print(messageDecoded)

