# EasyAsciiEncrypt
Easily encrypt any ASCII text data with a text key.
Simple as that.

**FEATURES:**

-EAE is ridiculously easy to use! Anyone with a fundamental understanding of python can utilize it!

-EAE adds salt to encryption/decrpytion and manages it seemlessly

-EAE obfuscates all string data, and is very secure

-EAE is customizable, settings can be adjusted easily.

-EAE is constantly being improved!


**INSTALLATION:**

Open your terminal and type...
```
pip install git+https://github.com/NCKLS/EasyAsciiEncrypt
```


**USAGE:**

Simply import the module and use the encrypt/decrypt functions to return encrypted or decrypted text.
The function works as so...


encrypt(plainTextHere, keyHere) -> Returns encrypted text (with salt by default)

decrypt(encryptedTextHere, keyHere) -> Returns decrypted text (removing salt by default)

```
import EasyAsciiEncrypt

encryptedText = EasyAsciiEncrypt.encrypt("This is plain text", "This is the key")
decryptedText = EasyAsciiEncrypt.decrypt(encryptedText, "This is the key")
print(encryptedText)
>>>{+DH/hX5UJ|x>GoCMjI/}@/HR}jN#| {6O7PHrL3!2]NAXwEgU}P2(+ECAA
>>> 2;tPXkp["!\KHJx&y50tpi}wbu4%
>>>\(wr!na/:FP+\5"p@[C7:wJJ#KXwpY|'9{z"l1nc;]cLt
print(decryptedText)
>>>This is plain text
```
or alternatively... (recommended)
```
from EasyAsciiEncrypt import *

encryptedText = encrypt("This is plain text", "This is the key")
decryptedText = decrypt(encryptedText, "This is the key")
print(encryptedText)
>>>{&riZMa|ag|'fsefvb!;}{?/)fj]KD 5]"m|paDu!Ly,-ogJ:S}57b]8!dI5 @Be
>>>y*h.e!b>n;IVQF{tpi}0`gDpFbXAr!t?7X6#N8k"$M_/4dM?L#(G)ZV*VhAz"lf&h$<V'R
print(decryptedText)
>>>This is plain text
```

If you would like to encrypt/decrypt text without adding salt to your encryption, simply set the salt argument to false.

```
from EasyAsciiEncrypt import *

encryptedText = encrypt("This is plain text", "This is the key", salt=False)
decryptedText = decrypt(encryptedText, "This is the key", salt=False)
print(encryptedText)
>>>{|} !} !tpi}r!"#z"
print(decryptedText)
>>>This is plain text
```

It is reccommended you do not remove salt, as it is less secure.
However, if you're looking to condense string size, it might be the right decision.
