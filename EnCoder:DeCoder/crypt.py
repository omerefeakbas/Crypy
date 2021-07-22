#Ascii encryption

def encode_ascii(message, password):
    message_encoded = ""
    for i in range(len(message)):
        message_encoded += chr(ord(message[i]) + ord(password[i%len(password)])%256)
    
    return message_encoded

def decode_ascii(message, password):
    message_decoded = ""
    for i in range(len(message)):
        message_decoded += chr(ord(message[i]) - ord(password[i%len(password)])%256)
    
    return message_decoded