# pyobfuscate.com---deobfuscator
Decrypts/deobfuscates pyobfuscate obfuscated python scripts. Goes to show how shit and probably pasted it is.

SINGLE LAYER - if your script is obfuscated only once, meaning it can be decrypted by running decryptor on it on the first attempt.
MULTIPLE LAYER - if your script is obfuscated more than once, meaning even after trying to decrypt it once (after trying to run single_Layer) on it, it's still obfuscated.

In the near future, I'll combine both into one file and make it so that you can choose the mode, single or multiple. I was just too lazy.

NOTE:
* IF YOUR OBFUSCATED SCRIPT IS SINGLE LAYER, USE single_layer_decryptor.py
* IF YOUR OBFUSCATED SCRIPT IS MULTIPLE LAYERS, USE multiple_layer_decryptor.py !

In case, in future, they change the proto or something, I'll update it.
You can pretty much bruteforce the number of layers yourself, just change "Decryption Factor" variable. It's currently `64`.
