from pwn import *

HOST = 'host_address_here.com' # change this to the server(if any)
PORT = 1337  # change this to the port that is supplied(if any)

io = remote(HOST, PORT) # connects to the service
#consider directly inputting the host and the port
#consider using a single char as variable e.g. p 
#p = remote('host', 1234)

io.recvuntil('Prompt here: ') # recives until prompt

payload = b'' # insert payload here
#example b"A"*64 sends 64 As, each char 1 being 1 byte 
#payload may need multiple parts
#payload = buffer + overwrite
#payload = buffer + canary + overwrite 
#overwrite = p64(int("0x00",16)); sends address in big endian iirc 
#NULL byte \x00 

io.sendline(payload) # sends your payload to the service

io.interactive() # allows you to interact with service manually

