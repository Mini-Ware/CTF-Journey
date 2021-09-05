from pwn import *

HOST = 'host_address_here.com' # change this to the server(if any)
PORT = 1337  # change this to the port that is supplied(if any)

io = remote(HOST, PORT) # connects to the service

io.recvuntil('Prompt here: ') # recives until prompt

payload = b'' # insert payload here

io.sendline(payload) # sends your payload to the service

io.interactive() # allows you to interact with service manually

