##  Web directory bruteforcers
- dirb(run dirb on terminal)
- dirbuster (requires GUI)
- gobuster (similar tool)
- dirsearch(faster alternative to dirb) [GitHub](https://github.com/maurosoria/dirsearch)
##  Web crawlers
- dirhunt [GitHub](https://github.com/Nekmo/dirhunt)
##  Packet utils
- burpsuite(requires GUI)
- wget
## XSS
- Stored XSS
> If an SVG with XSS payload is in an iframe or embed of a website, it can be executed
- Reflected XSS
> When queries to a website is handled and returned in an unsafe way
- DOM based XSS
> Client side attack, browser executes payload that didn't came from the server
## SQL Injection
- Union based attack
> Application displays the output of the query, allowing you to steal information from the database
- Error based attack
> Application returns an error with details about the query, helping you to craft queries to bypass checks
- Resources
> Sqlmap [GitHub](https://github.com/sqlmapproject/)</br>
> Practice [Website](http://mystery.knightlab.com/)
## Identify Vulnerablilities
- Steps to test for CSRF [Guide](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/05-Testing_for_Cross_Site_Request_Forgery)
- Steps to test for Broken Authentication [Guide](https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication)
