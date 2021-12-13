Cross Site Scripting (XSS)

Overview
Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.




So we gonna try to reproduse the XSS attack.We will replace the href for a picture to our 64base script:
>data:text/html; + base64(<script>alert("here we are");<?script>)

<img width="381" alt="Screen Shot 2021-12-10 at 2 43 06 PM" src="https://user-images.githubusercontent.com/64800542/145584193-294b6b43-6426-40e1-9b61-465d320514f9.png">

In the real life it might me a more dagereuse script (for stealing cookies...).

<img width="801" alt="Screen Shot 2021-12-10 at 2 47 35 PM" src="https://user-images.githubusercontent.com/64800542/145584169-64cea32e-6b29-4278-b3d7-52d9ac4e89bb.png">


Here you can find a cheatsheet "XSS prevention":
>https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html



