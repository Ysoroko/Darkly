# Darkly
Cybersecurity ethical hacking project

This project is a collaboration with [Kyrylo Kalinichenko](https://github.com/KyryloKalinichenko)

### Setup:
1) Download the provided .iso image and install Oracle Virtualbox
2) Since Oracle Virtualbox doesn't support .iso files, you can convert it to a supported format ".vdi" by running the following command in the terminal
  ``` Bash
  VBoxManage convertfromraw --format VDI "Complete-path-to-ISO-file" "Complete-path-to-VDI-file"
  
  ```
  
   - You might need to install "virtualbox" package.
   - If any other dependencies are needed, the terminal line will display the corresponding message

3) Once you have your ".vdi" file, In Oracle Virtualbox, click on "New" button 

    ![image](https://user-images.githubusercontent.com/36443074/144894861-8aa3047b-4035-41b9-9a4f-d4d52dfbf540.png)
    
   Click on "Next" button until you see this option. Tick the "Use an existing virtual hard disk drive" box
   
    ![image](https://user-images.githubusercontent.com/36443074/144894672-c036331c-0928-4510-8935-540d7ed4f02b.png)
  
   Click on the folder icon, then on "Add" and import your ".vdi" file to use it as an existing virtual hard disk file.
   
    ![image](https://user-images.githubusercontent.com/36443074/144896447-67af070d-33a1-4301-9316-abbf18f3105f.png)
    
4) Follow [this quick guide](https://condor.depaul.edu/glancast/443class/docs/vbox_host-only_setup.html) to create a Host-only network for your new virtual machine.
5) Once finished, click on "Settings" button on your newly created virtual machine and go to the "Network" section
   - In "Attached to" section, choose "Host-only Adapter"
   - If you followed the previous step correctly, the name of your new Host-only adapter should appear as an option in the field "Name"
   - In "Promiscuous Mode" select "Allow VMs"
   - Your window should now look like this:
  
    ![image](https://user-images.githubusercontent.com/36443074/144899986-414d24a7-ff5a-4fa4-9944-a36c13fc90b6.png)
  
 6) Press "OK". Your VM is ready, you can click on "Start" to launch it!
 7) At this point, you will get a window of the kind:
 
   ![image](https://user-images.githubusercontent.com/36443074/144900250-832d2b3d-66c0-44e1-9c98-e46784ff71a2.png)
 
 8) Just navigate to the IP address provided in your browser and you will get on the homepage on the website you need to break!

  ![image](https://user-images.githubusercontent.com/36443074/144901055-b982704c-300e-4513-b2fb-d5684fa11da7.png)



