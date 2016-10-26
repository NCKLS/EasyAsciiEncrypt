# EasyAsciiEncrypt
Easily encrypt any ASCII text data with a text key.

**INSTALLATION:**

Open your terminal and type...
```
pip install git+https://github.com/NCKLS/EasyAsciiEncrypt
```

**USAGE:**

Simply import the module and use the encrypt/decrypt functions to return encrypted or decrypted text.
The function works as so...

encrypt(plainTextHere, keyHere) -> Returns encrypted text
decrypt(encryptedTextHere, keyHere) -> Returns decrypted text

```
import EasyAsciiEncrypt

encryptedText = EasyAsciiEncrypt.encrypt("This is plain text", "This is the key")
decryptedText = EasyAsciiEncrypt.decrypt(encryptedText, "This is the key")
print(encryptedText)
>>> {|} !} !tpi}r!"#z"
print(decryptedText)
>>> This is plain text
```
or alternatively... (recommended)
```
from EasyAsciiEncrypt import *

encryptedText = encrypt("This is plain text", "This is the key")
decryptedText = decrypt(encryptedText, "This is the key")
print(encryptedText)
>>> {|} !} !tpi}r!"#z"
print(decryptedText)
>>> This is plain text
```
