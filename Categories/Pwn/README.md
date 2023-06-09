## What is binary exploitation?
- introduction [website](https://guyinatuxedo.github.io/00-intro/index.html) [website](https://vickieli.dev/binary%20exploitation/intro-to-reverse-engineering/)

## Exploitation
- Exploit Database [Website](https://www.exploit-db.com/)
## Restricted shell
- Usually done with rbash
- Look for binaries you can execute and check its functionalities to see if you can take advantage of anything
## Privilege escalation
- Check binaries for SUID permission bit
- Kernel bugs
## Binary exploitation tools
- pwntools [GitHub](https://github.com/Gallopsled/pwntools)
- pwndbg [GitHub](https://github.com/pwndbg/pwndbg)
- GEF [GitHub](https://github.com/hugsy/gef)
## Types of binary exploitation
Usually caused by buffer overflow/format string vulnerabilities
- Stack based
> Overwrite return address on stack to redirect code execution (Only for x86 binaries)
- Heap based
> Use after free
### Format string vulnerability
> Putting user input into functions that can take in format specifiers can potentially be exploited
