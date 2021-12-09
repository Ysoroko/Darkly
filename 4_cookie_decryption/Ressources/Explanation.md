# Cookie Decryption Breach
The breach related to the cookie encryption on the main webpage

### Explanation:
- On main webpage if we right click and go to Inspect -> Application -> Cookies (Google Chrome), we can see the following line:

  ![image](https://user-images.githubusercontent.com/36443074/145225971-0a83943c-4d74-4008-9c54-ebb5148e87ec.png)

- The name and the size of the value suggests us there is something to do here 
- We can try to decrypt the value using different tools to realize that it is encrypted in MD5 format and it is equal to "false"
- All we need to do is encode "true" in MD5 format, modify the value field and refresh the page
- The flag will pop up as an alert

### How to fix:
- MD5 is the weekest encryption method there is. Use something more robust (SHA / BLAKE)
