'''
Simple Python script demonstrating proof of work using SHA-256

- You can use `pycryptodome` as the crypto provider.
- Install it with:
    `pip install pycryptodome`
'''
import os
import binascii
from Crypto.Hash import SHA256

# How many leading zeros are required for an answer to be accepted
DIFFICULTY = 24

challenge = os.urandom(32)
answer = os.urandom(32)

while True:
  # compute SHA256 on the challenge + answer
  h = SHA256.new()
  h.update(challenge + answer)
  md = h.digest()

  # check how many leading zeros there are
  n = int.from_bytes(md, byteorder='big', signed=False)
  for i in range(DIFFICULTY):
    if (n >> (255 - i)) & 1:
      break
  else:
    break

  # try the digest as the next answer
  answer = md

print('Challenge:')
print(binascii.hexlify(challenge))

print('Answer:')
print(binascii.hexlify(answer))

print('Hash:')
print(binascii.hexlify(md))