# Forgotten Password Breach
The breach related to the forgotten password page

![image](https://user-images.githubusercontent.com/36443074/145016250-87d8c2cc-f08f-42c5-8125-46c2ff1d46fe.png)

### Explanation:
- On the homepage when we press "Sign In" button and then click on "I forgot my password" we get to the webpage you see above
- If we inspect the source code, we can see that there is a hidden input field, with a fixed value for an email:
    ![image](https://user-images.githubusercontent.com/36443074/145016589-5c43dfd4-a2cf-483e-bd17-ca280e23b7c3.png)
- If we modify the email in this field, the forgotten password (or the recovery procedure) can instead be sent to our own email address
- This can allow us to recover passwords from website users

### How to fix:
- Instead of sending it to the constant-value email address, we can simply use an input box with a user's email address
