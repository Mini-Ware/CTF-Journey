## Networking
- Nmap [Website](https://nmap.org/)
- Ncat [Website](https://nmap.org/ncat/)
- Ettercap [Website](https://www.ettercap-project.org/)
- Metasploit [Website](https://www.metasploit.com)/[GitHub](https://github.com/rapid7/metasploit-framework)
## Subnet classes

- IP subnet calculator [Website](https://www.calculator.net/ip-subnet-calculator.html)

> Subnet mask shows which octets are the same in a network

|Class|Subnet mask|Range|
|:---:|:---:|:---:|
|A|255.0.0.0|0.0.0.0 - 127.255.255.255|
|B|255.255.0.0|128.0.0.0 - 191.155.255.255|
|C|255.255.255.0|192.0.0.0 - 223.255.255.255|
|D|NA|224.0.0.0 - 239.255.255.255|
|E|NA|240.0.0.0 - 255.255.255.255|

> 127.x.x.x are loopback addresses (localhost)

> Class A gives the most host but least network while class C gives the most network but least host
## Public vs Private IP addresses
- You need a public IP address to access the internet
- Devices in a network are given private IP addresses
- Those addresses are converted into a public IP address by NAT (Network Address Translation)
- This conversion is done in your router for you to access the internet
- Public addresses are given to you by your ISP (Internet service provider)

## HTTPS Proxy tool
- mitmproxy [Website](https://mitmproxy.org/)
- BurpSuite [Website](https://portswigger.net/burp)
