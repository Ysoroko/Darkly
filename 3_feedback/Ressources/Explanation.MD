# Feedback Breach
The breach related to the feedback page

![image](https://user-images.githubusercontent.com/36443074/145081193-523ef1a7-a327-459f-97f7-99f7333ed272.png)



### Explanation:
- On this webpage we can input the name and the message
- Both fields are protected with functions which display an alert when you leave them empty
- However, there is an error in source code, function name is badly written
- You can see in the images below that the function "validate form" expects an "mtxMessage" but below the form is defined as "mtx**t**Message"
![image](https://user-images.githubusercontent.com/36443074/145081765-78fb4948-fc35-45ff-b5f7-f7f29f260dbd.png)
![image](https://user-images.githubusercontent.com/36443074/145081905-aa01a25b-deae-4a05-b3ec-17ba259f6ab4.png)
- This typo makes is to that when we enter an empty message with a valid name (for example, "l" in the name field"), it is considered valid


### How to fix:
- Just fix the typo

