# Different encrypthon methods covered here
- change of base
- XOR
- URL encoding

# base
there are many types of bases,
base2, base8, base10, base16, base64 and more!
`base10` is what we are used to, it has a range from 1-9
`base2` is what computers at its core uses, it has a range from 0-1

# XOR cyphers
XOR cyphers are intresting
```python
X ^ Y = z
X ^ z = Y
Y ^ z = X
```
therefore, if you have two of the XOR values, you are able to find the last unknown value

# URL encoding
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
