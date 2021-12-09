# Login brute force breach
The breach related to the login page

![image](https://user-images.githubusercontent.com/36443074/145256789-74f1fbf0-afb0-4d23-9827-24a9fd71a7a1.png)

### Explanation:
- On this webpage we can input the login and the password
- Very quickly by running several commands we can understand that these fields are not vulnerable to SQL injections
- However, when we type in an incorrect password, we can see that the webpage uses the input to access the next page
  
  ![image](https://user-images.githubusercontent.com/36443074/145258253-313e1e5f-767d-45dc-a41e-5859db6a0f3c.png)
 
- Also we know that on this webpage we have a very specific image on screen and in our source code: "images/WrongAnswer.gif":

  ![image](https://user-images.githubusercontent.com/36443074/145401132-601d7606-e550-42a0-b3b7-c9fb8c8b0194.png)
 
  ![image](https://user-images.githubusercontent.com/36443074/145401163-f14ee23a-037e-4f15-8849-12c3754b9c85.png)

- We can use this to brute force the login process!
- We used the top most used usernames and passwords from [OWASP SecLists](https://github.com/danielmiessler/SecLists)
- Using a simple script, we are capable to try every combination of most used passwords and usernames and if we don't see the "Wrong Answer" image
  on screen, it means that we succesfully logged in!
- Here the script shows us all the possible logins detected:
 
  ![image](https://user-images.githubusercontent.com/36443074/145259668-f75efbc9-4aea-4d42-9f29-7afb2e4e4e76.png)

- Any of these usernames with the password "shadow" will get us to the login page!

### How to fix:
- Use more robust username and password
