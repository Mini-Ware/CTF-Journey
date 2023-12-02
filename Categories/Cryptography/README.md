# Tools
- RsaCTFTool [GitHub](https://github.com/Ganapati/RsaCtfTool)
- XORtool [GitHub](https://github.com/hellman/xortool)
- hash_extender [GitHub](https://github.com/iagox86/hash_extender)
- FeatherDuster [GitHub](https://github.com/nccgroup/featherduster)
- CyberChef (View Strings) [Online Tool](https://gchq.github.io/CyberChef/)
- dCode (Cipher Identifier) [Online Tool](https://www.dcode.fr/cipher-identifier)
- fernet (Type of encryption) [Online Tool](https://asecuritysite.com/encryption/ferdecode)
- Hashcat [GitHub](https://github.com/hashcat/hashcat)
- John the Ripper [GitHub](https://github.com/openwall/john)
- randcrack (predict Python `random` numbers) [PyPi](https://pypi.org/project/randcrack/)
- Orphcrack

# Different encryption methods covered here
- change of base
- URL encoding
- XOR
- block ciphers
- DES
- RSA

## base
there are many types of bases,
base2, base8, base10, base16, base64 and more!
- `base2` also known as binary, it has a range from 0-1
- `base8` also known as octal.
- `base10` is what we are used to, it has a range from 1-9
- `base16` also known as hexadecimal, can be found in bits of two
- `base64` is easily spotted through having equal signs at the end
[note: may not be seen all the time]

## URL encoding
can be indentified easily.
Starts with % and two values following it
e.g.
```python
A: %41
B: %42
C: %43
```
as you can see, it follows the ascii value system.
URL encoding [website](https://onlineasciitools.com/url-encode-ascii)

## XOR cyphers
XOR cyphers are intresting
```python
X ^ Y = z
X ^ z = Y
Y ^ z = X
```
therefore, if you have two of the XOR values, you are able to find the last unknown value

## block ciphers

## DES

## RSA
Typically, simpler challenges can be solved with RsaCTFTool [GitHub](https://github.com/Ganapati/RsaCtfTool)

## One Time Pad (OTP)
