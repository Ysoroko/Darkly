# Social Media Redirection breach
The breach related to the social media redirection buttons on every webpage

![image](https://user-images.githubusercontent.com/36443074/145402740-142f0875-4c01-42d4-8f83-436d0bb6496a.png)

### Explanation:
- When we inspect the source code related to these buttons, we can see the following:
  - Twitter example:
  
    ![image](https://user-images.githubusercontent.com/36443074/145402856-dcbc09ea-f257-465b-8b8d-c1216d3b990f.png)
 
- Instead of simply providing a link to the desired redirection webpage, clicking on this button will instead send a request to the server
- We can send our own requests which may overload the server or make it do some undesired operations
- We can for example modify the source code to redirect us elsewhere, which will give us the flag

   ![image](https://user-images.githubusercontent.com/36443074/145403496-588ff0b8-ffe4-4134-8eb7-907768cf641a.png)


### How to fix:
- Provide a direct link instead of running the redirection through the server
