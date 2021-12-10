Cross Site Scripting (XSS)

Overview
Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

>https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html


So we gonna try to reproduse the DOS XSS:

>As defined by Amit Klein, who published the first article about this issue [1], DOM Based XSS is a form of XSS where the entire tainted data flow from source to >sink takes place in the browser, i.e., the source of the data is in the DOM, the sink is also in the DOM, and the data flow never leaves the browser. For >example, the source (where malicious data is read) could be the URL of the page (e.g., document.location.href), or it could be an element of the HTML, and the >sink is a sensitive method call that causes the execution of the malicious data (e.g., document.write).”

<img width="801" alt="Screen Shot 2021-12-10 at 2 47 35 PM" src="https://user-images.githubusercontent.com/64800542/145584169-64cea32e-6b29-4278-b3d7-52d9ac4e89bb.png">


<img width="381" alt="Screen Shot 2021-12-10 at 2 43 06 PM" src="https://user-images.githubusercontent.com/64800542/145584193-294b6b43-6426-40e1-9b61-465d320514f9.png">
