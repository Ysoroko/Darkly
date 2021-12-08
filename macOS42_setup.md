### MacOS 42 network iMacs setup:
1) Download the provided .iso image and install Oracle Virtualbox via Managed Software Center if needed.

    You can use "goinfre" if you don't have enough space on the device for the VM.
  
2) Since Oracle Virtualbox doesn't support .iso files, you can convert it to a supported format ".vdi" by running the following command in the terminal
  ``` Bash
  VBoxManage convertfromraw --format VDI "Complete-path-to-ISO-file" "Complete-path-to-VDI-file"
  
  ```

3) Once you have your ".vdi" file, In Oracle Virtualbox, click on "New" button 

    ![image](https://user-images.githubusercontent.com/36443074/145214766-f756dffa-47ed-4ce3-962b-386741ffce77.png)

   Enter your preferred VM name in the "Name" field and tick the "Use an existing virtual hard disk drive" box
   
    ![image](https://user-images.githubusercontent.com/36443074/145214982-365a261e-ec5f-434a-b4aa-3b5cf5d455e0.png)
  
   Click on the folder icon, then on "Add" and import your ".vdi" file to use it as an existing virtual hard disk file.
   
    ![image](https://user-images.githubusercontent.com/36443074/144896447-67af070d-33a1-4301-9316-abbf18f3105f.png)
    
   Press "Create".
    
4) Follow [this quick guide](https://carleton.ca/scs/2019/creating-a-new-host-only-adapter-in-virtualbox/) to create a Host-only network for your new virtual machine.
5) Once finished, click on "Settings" button on your newly created virtual machine and go to the "Network" section
   - In "Attached to" section, choose "Host-only Adapter"
   - If you followed the step 4 correctly, the name of your new Host-only adapter should appear as an option in the field "Name"
   - In "Promiscuous Mode" select "Allow VMs"
   - Your window should now look like this:
   
      ![image](https://user-images.githubusercontent.com/36443074/145215711-f86536e0-025f-4563-8382-0a4b0b2ae7f2.png)

  
 6) Press "OK". Your VM is ready, you can click on "Start" to launch it!
 7) At this point, you will get a window of the kind:
 
   ![image](https://user-images.githubusercontent.com/36443074/144900250-832d2b3d-66c0-44e1-9c98-e46784ff71a2.png)
 
 8) Just navigate to the IP address provided in your browser and you will get on the homepage of the website you need to break!

  ![image](https://user-images.githubusercontent.com/36443074/144901055-b982704c-300e-4513-b2fb-d5684fa11da7.png)

