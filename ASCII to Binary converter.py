import binascii

output = bin(int.from_bytes('C'.encode(), 'big'))

print(output)

